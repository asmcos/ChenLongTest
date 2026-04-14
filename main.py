#!/usr/bin/env python3
"""
StarryOS 自动化测试脚本
通过 QEMU 的串口 TCP 连接发送命令并验证输出
每次启动测试在 logs 下新建会话时间戳目录：各命令串口输出为单独 .log；
控制台 INFO/ERROR 与之一并写入同目录 run.log（总汇报）。
"""

import argparse
import logging
import os
import sys
import time
from datetime import datetime
from typing import Any, Dict, List, Optional, Tuple, Union

from harness import CustomTest, QemuSerialClient, TestCase, safe_filename

_LOG_FMT = "%(asctime)s - %(levelname)s - %(message)s"

# 控制台：basicConfig 仅在 root 无 handler 时生效
logging.basicConfig(level=logging.INFO, format=_LOG_FMT)
logger = logging.getLogger(__name__)


def _attach_session_report_log(session_dir: str) -> Tuple[str, logging.Handler]:
    """
    在 root logger 上追加文件 handler，使控制台与 logs/<会话>/run.log 内容一致（总汇报）。
    """
    path = os.path.join(session_dir, "run.log")
    fh = logging.FileHandler(path, encoding="utf-8")
    fh.setLevel(logging.INFO)
    fh.setFormatter(logging.Formatter(_LOG_FMT))
    logging.getLogger().addHandler(fh)
    return path, fh


def _detach_session_report_log(fh: logging.Handler) -> None:
    root = logging.getLogger()
    if fh in root.handlers:
        root.removeHandler(fh)
    fh.close()

# 创建 logs 目录
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

SERIAL_HOST = "192.168.123.33"

Runnable = Union[TestCase, CustomTest]


def test_case_from_spec(spec: Dict[str, Any]) -> TestCase:
    """将 busybox 等子模块中的 TEST 字典转为 TestCase（字段统一）。"""
    return TestCase(
        name=spec["name"],
        cmd=spec["cmd"],
        expected_substring=spec.get("expected_substring"),
        expect_non_empty=bool(spec.get("expect_non_empty", True)),
        timeout=float(spec.get("timeout", 2.0)),
        clean=spec.get("clean"),
    )


def load_test_suite(
    name: Optional[str] = None,
    order: Optional[int] = None,
) -> List[Runnable]:
    """
    动态发现并加载 busybox/ 下各 test_*.py：有 run() 走定制，否则走默认 TestCase。
    name / order 二选一或同时指定（同时指定时须同一用例同时满足）；均为 None 时跑全部。
    """
    from busybox import discover_loaded_tests

    suite: List[Runnable] = []
    for spec, run_fn in discover_loaded_tests():
        if name is not None and spec.get("name") != name:
            continue
        if order is not None and int(spec.get("order", -1)) != order:
            continue
        if run_fn is not None:
            suite.append(CustomTest(spec, run_fn))
        else:
            suite.append(test_case_from_spec(spec))
    return suite


def parse_args(argv: Optional[List[str]] = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="StarryOS BusyBox 串口自动化测试（默认跑全部用例）",
    )
    p.add_argument(
        "-t",
        "--test",
        metavar="NAME",
        dest="test_name",
        help="只跑一个用例：与 TEST 字典中 name 一致，例如 busybox_du",
    )
    p.add_argument(
        "--order",
        type=int,
        metavar="N",
        dest="order",
        help="只跑一个用例：与 TEST 字典中 order 一致，例如 57",
    )
    return p.parse_args(argv)


def save_output_to_file(cmd: str, output: str, test_name: str, session_dir: str) -> str:
    """将命令输出保存到本次会话目录下的文件，返回文件路径（文件名不含时间戳）"""
    filename = f"{safe_filename(test_name)}.log"
    filepath = os.path.join(session_dir, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"Command: {cmd}\n")
        f.write(f"Timestamp: {datetime.now().isoformat()}\n")
        f.write("=" * 60 + "\n")
        f.write(output)
        f.write("\n" + "=" * 60 + "\n")
    logger.info(f"Output saved to {filepath}")
    return filepath


def run_test_cleanup(client: QemuSerialClient, test: Runnable) -> None:
    """执行单测自带 clean 命令；失败只记 warning，不影响主流程。"""
    clean_cmd = getattr(test, "clean", None)
    if not clean_cmd:
        return
    try:
        client.send_cmd(clean_cmd, timeout=2.0)
        logger.info(f"Cleanup done: {test.name} -> {clean_cmd}")
    except Exception as e:
        logger.warning(f"Cleanup failed for {test.name}: {e}")


def run_tests(client: QemuSerialClient, tests: List[Runnable], session_dir: str) -> None:
    """运行测试套件；会话目录已存在，每个命令输出保存为该目录下的单独文件。"""
    logger.info(f"Starting {len(tests)} tests...")
    logger.info("Cleanup policy: run per-test TEST['clean'] if provided")
    passed = 0
    failed = 0
    for test in tests:
        logger.info(f"Running test: {test.name} -> {test.cmd}")
        ok, msg, output = test.run(client)
        save_output_to_file(test.cmd, output, test.name, session_dir)
        if ok:
            logger.info(f"✅ PASS: {test.name} - {msg}")
            passed += 1
        else:
            logger.error(f"❌ FAIL: {test.name} - {msg}")
            failed += 1
        run_test_cleanup(client, test)
        time.sleep(0.3)
    logger.info(f"Test summary: {passed} passed, {failed} failed, total {len(tests)}")


def main(argv: Optional[List[str]] = None) -> None:
    args = parse_args(argv)
    session_ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    session_dir = os.path.join(LOG_DIR, session_ts)
    os.makedirs(session_dir, exist_ok=True)
    report_path, report_fh = _attach_session_report_log(session_dir)
    logger.info(f"Session log directory: {session_dir}")
    logger.info(f"Console mirror / full report: {report_path}")

    suite = load_test_suite(
        name=args.test_name,
        order=args.order,
    )
    if args.test_name is not None or args.order is not None:
        if not suite:
            logger.error(
                "No test matches the filter (--test / --order). "
                "Check busybox/test_*.py TEST['name'] and TEST['order']."
            )
            _detach_session_report_log(report_fh)
            sys.exit(1)
        logger.info(
            f"Single-test mode: name={args.test_name!r} order={args.order!r} -> {len(suite)} case(s)"
        )
    if not suite:
        logger.warning("No tests discovered under busybox/; add busybox/test_*.py with TEST dict.")
    client = QemuSerialClient(host=SERIAL_HOST, port=4444, timeout=1.0)
    try:
        client.connect()
        client.send_cmd("")  # 唤醒 shell
        run_tests(client, suite, session_dir)
    except ConnectionRefusedError:
        logger.error(
            "Cannot connect to QEMU. Please start QEMU with: -serial tcp:127.0.0.1:4444,server,nowait"
        )
    except Exception as e:
        logger.exception(f"Unexpected error: {e}")
    finally:
        client.close()
        _detach_session_report_log(report_fh)


if __name__ == "__main__":
    main()
