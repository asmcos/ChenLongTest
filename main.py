#!/usr/bin/env python3
"""
StarryOS 自动化测试脚本
通过 QEMU 的串口 TCP 连接发送命令并验证输出
每次启动测试在 logs 下新建会话时间戳目录，各命令输出写入该目录下的独立文件
"""

import socket
import re
import time
import logging
import os
from datetime import datetime
from typing import Any, Dict, List, Tuple, Optional

# 配置日志（控制台输出）
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# ANSI 转义序列正则（颜色、光标位置等）
ANSI_ESCAPE = re.compile(r'\x1b\[[0-9;]*[a-zA-Z]')

# 创建 logs 目录
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)


def safe_filename(text: str) -> str:
    """将字符串转换为安全的文件名（替换特殊字符）"""
    return re.sub(r'[\\/*?:"<>|]', '_', text)[:50]  # 限制长度

SERIAL_HOST = '192.168.123.33'

class QemuSerialClient:
    """QEMU 串口 TCP 客户端"""

    def __init__(self, host: str = SERIAL_HOST, port: int = 4444, timeout: float = 1.0):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.sock: Optional[socket.socket] = None

    def connect(self) -> None:
        """建立 TCP 连接并清空缓冲区"""
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
        """清空 socket 接收缓冲区"""
        if not self.sock:
            return
        try:
            while True:
                self.sock.recv(4096)
        except socket.timeout:
            pass
        except Exception as e:
            logger.warning(f"Flush error: {e}")

    def send_cmd(self, cmd: str, timeout: Optional[float] = None) -> str:
        """
        发送命令并返回输出（已过滤 ANSI 转义序列）
        """
        if not self.sock:
            raise ConnectionError("Not connected. Call connect() first.")

        old_timeout = self.sock.gettimeout()
        if timeout is not None:
            self.sock.settimeout(timeout)

        try:
            self._flush()
            self.sock.send((cmd + '\n').encode())
            logger.debug(f"Sent command: {cmd}")

            output = b''
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

            text = output.decode('utf-8', errors='replace')
            text = ANSI_ESCAPE.sub('', text)

            lines = text.splitlines()
            if lines and lines[0].strip() == cmd:
                lines = lines[1:]

            return '\n'.join(lines).strip()

        finally:
            if timeout is not None:
                self.sock.settimeout(old_timeout)

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


class TestCase:
    """单个测试用例"""
    def __init__(self, name: str, cmd: str, expected_substring: Optional[str] = None,
                 expect_non_empty: bool = True, timeout: float = 2.0):
        self.name = name
        self.cmd = cmd
        self.expected_substring = expected_substring
        self.expect_non_empty = expect_non_empty
        self.timeout = timeout

    def run(self, client: QemuSerialClient) -> Tuple[bool, str, str]:
        """
        执行测试，返回 (通过与否, 详细信息, 输出内容)
        """
        try:
            output = client.send_cmd(self.cmd, timeout=self.timeout)
            if self.expected_substring is not None:
                if self.expected_substring in output:
                    return True, f"Found expected substring: '{self.expected_substring}'", output
                else:
                    return False, f"Expected substring not found. Output preview: {output[:200]}", output
            if self.expect_non_empty:
                if output.strip():
                    return True, f"Output non-empty (length {len(output)})", output
                else:
                    return False, "Output is empty", output
            return True, "OK", output
        except Exception as e:
            return False, f"Exception: {e}", ""


def test_case_from_spec(spec: Dict[str, Any]) -> TestCase:
    """将 busybox 等子模块中的 TEST 字典转为 TestCase（字段统一）。"""
    return TestCase(
        name=spec["name"],
        cmd=spec["cmd"],
        expected_substring=spec.get("expected_substring"),
        expect_non_empty=bool(spec.get("expect_non_empty", True)),
        timeout=float(spec.get("timeout", 2.0)),
    )


def load_test_suite() -> List[TestCase]:
    """动态发现并加载 busybox/ 下各 test_*.py 的 TEST 定义。"""
    from busybox import discover_test_specs

    return [test_case_from_spec(s) for s in discover_test_specs()]


def save_output_to_file(cmd: str, output: str, test_name: str, session_dir: str) -> str:
    """将命令输出保存到本次会话目录下的文件，返回文件路径（文件名不含时间戳）"""
    filename = f"{safe_filename(test_name)}.log"
    filepath = os.path.join(session_dir, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(f"Command: {cmd}\n")
        f.write(f"Timestamp: {datetime.now().isoformat()}\n")
        f.write("=" * 60 + "\n")
        f.write(output)
        f.write("\n" + "=" * 60 + "\n")
    logger.info(f"Output saved to {filepath}")
    return filepath


def run_tests(client: QemuSerialClient, tests: List[TestCase]) -> None:
    """运行测试套件；先创建会话时间戳目录，每个命令输出保存为该目录下的单独文件"""
    session_ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    session_dir = os.path.join(LOG_DIR, session_ts)
    os.makedirs(session_dir, exist_ok=True)
    logger.info(f"Session log directory: {session_dir}")
    logger.info(f"Starting {len(tests)} tests...")
    passed = 0
    failed = 0
    for test in tests:
        logger.info(f"Running test: {test.name} -> command: {test.cmd}")
        ok, msg, output = test.run(client)
        # 保存输出到文件（无论成功或失败）
        save_output_to_file(test.cmd, output, test.name, session_dir)
        if ok:
            logger.info(f"✅ PASS: {test.name} - {msg}")
            passed += 1
        else:
            logger.error(f"❌ FAIL: {test.name} - {msg}")
            failed += 1
        time.sleep(0.3)  # 命令间隔
    logger.info(f"Test summary: {passed} passed, {failed} failed, total {len(tests)}")


def main():
    suite = load_test_suite()
    if not suite:
        logger.warning("No tests discovered under busybox/; add busybox/test_*.py with TEST dict.")
    client = QemuSerialClient(host=SERIAL_HOST, port=4444, timeout=1.0)
    try:
        client.connect()
        client.send_cmd("")  # 唤醒 shell
        run_tests(client, suite)
    except ConnectionRefusedError:
        logger.error("Cannot connect to QEMU. Please start QEMU with: -serial tcp:127.0.0.1:4444,server,nowait")
    except Exception as e:
        logger.exception(f"Unexpected error: {e}")
    finally:
        client.close()


if __name__ == '__main__':
    main()
