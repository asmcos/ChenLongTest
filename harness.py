#!/usr/bin/env python3
"""
QEMU 串口客户端与默认 TestCase；供 main 与 busybox 各子模块共用，避免循环 import。
"""

from __future__ import annotations

import logging
import re
import socket
import time
from typing import List, Optional, Tuple

logger = logging.getLogger(__name__)

ANSI_ESCAPE = re.compile(r"\x1b\[[0-9;]*[a-zA-Z]")


def safe_filename(text: str) -> str:
    return re.sub(r'[\\/*?:"<>|]', "_", text)[:50]


class QemuSerialClient:
    """QEMU 串口 TCP 客户端"""

    def __init__(self, host: str, port: int = 4444, timeout: float = 1.0):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.sock: Optional[socket.socket] = None

    def connect(self) -> None:
        if self.sock:
            self.close()
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.settimeout(self.timeout)
        self.sock.connect((self.host, self.port))
        logger.info(f"Connected to {self.host}:{self.port}")
        self._flush()

    def close(self) -> None:
        if self.sock:
            self.sock.close()
            self.sock = None
            logger.info("Connection closed")

    def _flush(self) -> None:
        if not self.sock:
            return
        try:
            while True:
                self.sock.recv(4096)
        except socket.timeout:
            pass
        except Exception as e:
            logger.warning(f"Flush error: {e}")

    def send_line(self, line: str) -> None:
        """发送一行（带换行），不自动读回显；用于交互场景。"""
        if not self.sock:
            raise ConnectionError("Not connected. Call connect() first.")
        self.sock.send((line + "\n").encode())
        logger.debug(f"Sent line: {line!r}")

    def read_until(
        self,
        marker: str,
        per_read_timeout: float = 0.5,
        max_total: float = 30.0,
    ) -> str:
        """
        持续读取直到输出中出现 marker，或超过 max_total 秒。
        用于交互：例如出现 Password: 后再 send_line 输入。
        """
        if not self.sock:
            raise ConnectionError("Not connected. Call connect() first.")
        deadline = time.monotonic() + max_total
        buf = b""
        while time.monotonic() < deadline:
            remain = deadline - time.monotonic()
            if remain <= 0:
                break
            self.sock.settimeout(min(per_read_timeout, remain))
            try:
                chunk = self.sock.recv(4096)
                if not chunk:
                    break
                buf += chunk
            except socket.timeout:
                continue
            text = ANSI_ESCAPE.sub("", buf.decode("utf-8", errors="replace"))
            if marker in text:
                return text
        return ANSI_ESCAPE.sub("", buf.decode("utf-8", errors="replace"))

    def send_cmd(self, cmd: str, timeout: Optional[float] = None) -> str:
        """发送一条命令，按超时收完一段输出（过滤 ANSI），适合非交互命令。"""
        if not self.sock:
            raise ConnectionError("Not connected. Call connect() first.")

        old_timeout = self.sock.gettimeout()
        if timeout is not None:
            self.sock.settimeout(timeout)

        try:
            self._flush()
            self.sock.send((cmd + "\n").encode())
            logger.debug(f"Sent command: {cmd}")

            output = b""
            while True:
                try:
                    chunk = self.sock.recv(4096)
                    if not chunk:
                        break
                    output += chunk
                except socket.timeout:
                    break
                except Exception as e:
                    logger.error(f"Receive error: {e}")
                    break

            text = output.decode("utf-8", errors="replace")
            text = ANSI_ESCAPE.sub("", text)

            lines = text.splitlines()
            if lines and lines[0].strip() == cmd:
                lines = lines[1:]

            return "\n".join(lines).strip()

        finally:
            if timeout is not None:
                self.sock.settimeout(old_timeout)

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


class TestCase:
    """默认：单条 cmd + 子串/非空校验"""

    def __init__(
        self,
        name: str,
        cmd: str,
        expected_substring: Optional[str] = None,
        expect_non_empty: bool = True,
        timeout: float = 2.0,
        clean: Optional[str] = None,
    ):
        self.name = name
        self.cmd = cmd
        self.expected_substring = expected_substring
        self.expect_non_empty = expect_non_empty
        self.timeout = timeout
        self.clean = clean

    def run(self, client: QemuSerialClient) -> Tuple[bool, str, str]:
        try:
            output = client.send_cmd(self.cmd, timeout=self.timeout)
            if self.expected_substring is not None:
                if self.expected_substring in output:
                    return True, f"Found expected substring: '{self.expected_substring}'", output
                return (
                    False,
                    f"Expected substring not found. Output preview: {output[:200]}",
                    output,
                )
            if self.expect_non_empty:
                if output.strip():
                    return True, f"Output non-empty (length {len(output)})", output
                return False, "Output is empty", output
            return True, "OK", output
        except Exception as e:
            return False, f"Exception: {e}", ""


class CustomTest:
    """子模块实现 run(client) 时的包装，与 TestCase 共用 name/cmd/run 接口。"""

    def __init__(
        self,
        spec: dict,
        run_fn,
    ):
        self.spec = spec
        self.run_fn = run_fn
        self.name = spec["name"]
        self.cmd = spec.get("cmd", f"[custom] {self.name}")
        self.clean = spec.get("clean")

    def run(self, client: QemuSerialClient) -> Tuple[bool, str, str]:
        return self.run_fn(client)
