#!/usr/bin/env python3
"""
QEMU 串口客户端与默认 TestCase；供 main 与 busybox 各子模块共用，避免循环 import。
"""

from __future__ import annotations

import logging
import re
import socket
import time
from typing import List, Optional, Sequence, Tuple

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
        # 每个用例内多次 send_cmd 的原文片段（归一化后、未做「删首行」处理），供日志对照交互界面
        self._test_capture_chunks: List[str] = []

    def begin_test_capture(self) -> None:
        self._test_capture_chunks.clear()

    def get_serial_transcript_for_log(self) -> str:
        """本次用例内所有 send_cmd 收到的串口原文拼接（含提示符、命令回显）。"""
        return "\n".join(self._test_capture_chunks)

    def connect(self) -> None:
        if self.sock:
            self.close()
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.settimeout(self.timeout)
        self.sock.connect((self.host, self.port))
        logger.info(f"Connected to {self.host}:{self.port}")
        self._flush()

    def probe_serial_forwards_stdout(self, timeout_sec: float = 4.0) -> bool:
        """检测 TCP 串口是否能看到命令的真实标准输出（而非仅有本地行编辑回显）。

        若 StarryOS/QEMU 只把「正在输入的一行」镜像到 TCP，而不转发子进程 stdout，则
        ``busybox id`` 的应答里不会出现 ``uid=``；此时原始字节往往只有命令回显与
        一段以 ``.`` 开头、空格被吃掉的伪回显行，与手边真实终端里能看到
        ``uid=0(...)`` 的行为不一致。依赖子串断言的用例会集体不可靠，需在串口/pty
        侧修复后再跑自动化。
        """
        if not self.sock:
            return False
        self.sock.send(b"busybox id\n")
        buf = b""
        deadline = time.monotonic() + timeout_sec
        old = self.sock.gettimeout()
        poll = 0.15
        idle_needed = 5
        idle = 0
        try:
            self.sock.settimeout(poll)
            while time.monotonic() < deadline:
                try:
                    chunk = self.sock.recv(4096)
                    if chunk:
                        buf += chunk
                        idle = 0
                        if b"uid=" in buf or b"gid=" in buf:
                            return True
                    else:
                        idle += 1
                        if buf and idle >= idle_needed:
                            break
                except socket.timeout:
                    idle += 1
                    if buf and idle >= idle_needed:
                        break
        finally:
            self.sock.settimeout(old)
        return b"uid=" in buf or b"gid=" in buf

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

    def recover_shell(self) -> None:
        """尽量回到交互 shell，再发下一条命令或 clean。

        若上一用例启动了仍占用前台的进程（典型如 ``busybox acpid``、或交互程序），
        ``send_cmd`` 会因超时先返回，但串口输入仍被该进程占用，后续字节不会交给 sh，
        表现为「不像在 shell 里」、管道/子串断言异常。连发若干次 Ctrl-C 并排空缓冲，
        以便回到提示符；不写入 ``_test_capture_chunks``（在 ``begin_test_capture`` 外调用）。
        """
        if not self.sock:
            return
        old = self.sock.gettimeout()
        try:
            self.sock.settimeout(0.12)
            for _ in range(5):
                self.sock.send(b"\x03")
                time.sleep(0.02)
            self.sock.send(b"\n")
            time.sleep(0.05)
            self._flush()
        finally:
            self.sock.settimeout(old)

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
            text = self._normalize_serial_text(buf)
            if marker in text:
                return text
        return self._normalize_serial_text(buf)

    @staticmethod
    def _normalize_serial_text(raw: bytes) -> str:
        """把串口字节流变成可读多行文本。

        交互 shell 常用 ``\\r`` 将光标移回行首并重绘；若把裸 ``\\r`` 直接换成 ``\\n``，
        会把同一物理行拆成多行并产生「空格被吃掉」的假乱码。此处按「同一行内最后一次
        ``\\r`` 之后为当前可见内容」处理（与常见串口日志工具一致）。
        """
        text = raw.decode("utf-8", errors="replace")
        text = ANSI_ESCAPE.sub("", text)
        text = text.replace("\r\n", "\n")
        lines_out: List[str] = []
        for line in text.split("\n"):
            if "\r" in line:
                line = line.split("\r")[-1]
            lines_out.append(line)
        return "\n".join(lines_out)

    @staticmethod
    def _strip_leading_cmd_echo(lines: List[str], cmd: str) -> List[str]:
        """去掉首行里 shell 提示符 + 回显命令，便于与 cmd 对齐做子串判断。"""
        if not lines:
            return lines
        s0 = lines[0].strip()
        if s0 == cmd:
            return lines[1:]
        for prefix in ("starry:~#", "starry #", "~#"):
            if s0.startswith(prefix):
                rest = s0[len(prefix) :].strip()
                if rest == cmd:
                    return lines[1:]
        return lines

    def send_cmd(
        self,
        cmd: str,
        timeout: Optional[float] = None,
        wait_for: Optional[str] = None,
    ) -> str:
        """发送一条命令，收串口输出（过滤 ANSI），适合非交互命令。

        管道/较慢命令可能分多段到达；旧实现「第一次 recv 超时即结束」会丢掉后续输出。
        现改为短超时轮询，直到连续若干次无新数据（认为一帧输出结束），且受总时长上限约束。

        wait_for: 若设置，则**在缓冲区中出现该子串之前**不因短暂空闲而结束（避免串口上
        回显先返回、真实输出晚到半拍被截断）。出现子串后再等若干次空闲以收齐尾部的 prompt。
        """
        if not self.sock:
            raise ConnectionError("Not connected. Call connect() first.")

        old_timeout = self.sock.gettimeout()
        # 等特定输出时总时长放宽
        base = max(float(timeout or 5.0), 3.0)
        max_total = max(base, 12.0) if wait_for else base
        poll = 0.12
        idle_needed = 3

        try:
            # 不在发命令前 _flush()：否则会丢掉缓冲区里尚未读取的 starry:~# 提示符，
            # 日志里就看不到「像手敲终端」的完整一行。
            self.sock.settimeout(poll)
            self.sock.send((cmd + "\n").encode())
            logger.debug(f"Sent command: {cmd}")

            output = b""
            idle_rounds = 0
            deadline = time.monotonic() + max_total

            while time.monotonic() < deadline:
                try:
                    chunk = self.sock.recv(4096)
                    if chunk:
                        output += chunk
                        idle_rounds = 0
                    else:
                        idle_rounds += 1
                        dec = self._normalize_serial_text(output)
                        has = wait_for is None or wait_for in dec
                        if has and output and idle_rounds >= idle_needed:
                            break
                        if not has:
                            continue
                        if output and idle_rounds >= idle_needed:
                            break
                except socket.timeout:
                    idle_rounds += 1
                    dec = self._normalize_serial_text(output)
                    has = wait_for is None or wait_for in dec
                    if has and output and idle_rounds >= idle_needed:
                        break
                    if not has:
                        continue
                    if output and idle_rounds >= idle_needed:
                        break
                except Exception as e:
                    logger.error(f"Receive error: {e}")
                    break

            text = self._normalize_serial_text(output)
            self._test_capture_chunks.append(text)

            lines = text.splitlines()
            lines = self._strip_leading_cmd_echo(lines, cmd)

            return "\n".join(lines).strip()

        finally:
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
        fail_if_substrings: Optional[Sequence[str]] = None,
        wait_for: Optional[str] = None,
        order: Optional[int] = None,
    ):
        self.name = name
        self.cmd = cmd
        self.expected_substring = expected_substring
        self.expect_non_empty = expect_non_empty
        self.timeout = timeout
        self.clean = clean
        self.fail_if_substrings: Tuple[str, ...] = tuple(fail_if_substrings or ())
        self.wait_for = wait_for
        self.order = order

    def run(self, client: QemuSerialClient) -> Tuple[bool, str, str]:
        try:
            output = client.send_cmd(
                self.cmd,
                timeout=self.timeout,
                wait_for=self.wait_for,
            )
            for bad in self.fail_if_substrings:
                if bad in output:
                    return (
                        False,
                        f"Output contains failure marker {bad!r}",
                        output,
                    )
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
        o = spec.get("order")
        self.order: Optional[int] = int(o) if o is not None else None

    def run(self, client: QemuSerialClient) -> Tuple[bool, str, str]:
        return self.run_fn(client)
