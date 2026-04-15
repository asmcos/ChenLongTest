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
from typing import Any, Dict, List, Optional, Sequence, Tuple, Union

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


def runnable_order(test: Runnable) -> Optional[int]:
    """从 TestCase.order 或 CustomTest.spec['order'] 取序号，供日志与落盘。"""
    o = getattr(test, "order", None)
    if o is not None:
        return int(o)
    spec = getattr(test, "spec", None)
    if isinstance(spec, dict):
        raw = spec.get("order")
        if raw is not None:
            return int(raw)
    return None


def parse_order_range(s: str) -> Tuple[int, int]:
    """``--order-range`` 参数：``1-13`` 或 ``13-1``（自动交换为闭区间）。"""
    s = s.strip()
    if "-" not in s:
        raise argparse.ArgumentTypeError("必须是 START-END，例如 1-13")
    a, _, b = s.partition("-")
    if not a.strip() or not b.strip():
        raise argparse.ArgumentTypeError("必须是 START-END，例如 1-13")
    lo, hi = int(a.strip()), int(b.strip())
    if lo > hi:
        lo, hi = hi, lo
    return (lo, hi)


def parse_orders(s: str) -> Tuple[int, ...]:
    """``--orders`` 参数：逗号分隔，如 ``1,4,6,19``；也接受 ``[1,4,6,19]`` 形式。"""
    s = s.strip()
    if s.startswith("[") and s.endswith("]"):
        s = s[1:-1].strip()
    if not s:
        raise argparse.ArgumentTypeError("至少给一个 order，例如 1,4,6,19 或 [1,4,6,19]")
    parts: List[int] = []
    for p in s.split(","):
        p = p.strip()
        if not p:
            continue
        parts.append(int(p))
    if not parts:
        raise argparse.ArgumentTypeError("至少给一个 order，例如 1,4,6,19")
    return tuple(parts)


def test_case_from_spec(spec: Dict[str, Any]) -> TestCase:
    """将 busybox 等子模块中的 TEST 字典转为 TestCase（字段统一）。"""
    fail_subs: List[str] = []
    if spec.get("fail_if_substrings"):
        fail_subs.extend(spec["fail_if_substrings"])
    elif spec.get("fail_if_substring"):
        fail_subs.append(spec["fail_if_substring"])
    o = spec.get("order")
    return TestCase(
        name=spec["name"],
        cmd=spec["cmd"],
        expected_substring=spec.get("expected_substring"),
        expect_non_empty=bool(spec.get("expect_non_empty", True)),
        timeout=float(spec.get("timeout", 2.0)),
        clean=spec.get("clean"),
        fail_if_substrings=fail_subs or None,
        wait_for=spec.get("wait_for"),
        order=int(o) if o is not None else None,
    )


def load_test_suite(
    name: Optional[str] = None,
    order: Optional[int] = None,
    order_range: Optional[Tuple[int, int]] = None,
    orders: Optional[Sequence[int]] = None,
) -> List[Runnable]:
    """
    动态发现并加载 busybox/ 下各 test_*.py：有 run() 走定制，否则走默认 TestCase。
    name 可与 order / order_range / orders 组合（同时满足）；order、order_range、orders
    三者只能传其一；均为 None 时跑全部。
    """
    from busybox import discover_loaded_tests

    order_set = frozenset(orders) if orders is not None else None
    suite: List[Runnable] = []
    for spec, run_fn in discover_loaded_tests():
        if name is not None and spec.get("name") != name:
            continue
        o = int(spec.get("order", -1))
        if order is not None and o != order:
            continue
        if order_range is not None:
            lo, hi = order_range
            if not (lo <= o <= hi):
                continue
        if order_set is not None and o not in order_set:
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
    p.add_argument(
        "--order-range",
        type=parse_order_range,
        metavar="START-END",
        dest="order_range",
        help="只跑 order 在闭区间内的用例，例如 1-13",
    )
    p.add_argument(
        "--orders",
        type=parse_orders,
        metavar="N,N,...",
        dest="orders",
        help="只跑列出的 order，逗号分隔，例如 1,4,6,19；也支持 [1,4,6,19]（须加引号）",
    )
    args = p.parse_args(argv)
    n = sum(
        1
        for x in (args.order, args.order_range, args.orders)
        if x is not None
    )
    if n > 1:
        p.error("--order、--order-range、--orders 只能任选其一")
    return args


def save_output_to_file(
    cmd: str,
    output: str,
    test_name: str,
    session_dir: str,
    raw_transcript: Optional[str] = None,
    order: Optional[int] = None,
) -> str:
    """将命令输出保存到本次会话目录下的文件，返回文件路径（文件名不含时间戳）。

    raw_transcript: send_cmd 收到的串口原文（含 starry:~# 与回显），便于与手动交互对照；
    output: 供子串断言的处理后文本（可能与原文在首行去重等方面不同）。
    order: 与 busybox TEST['order'] 一致，便于按序号检索日志。
    """
    filename = f"{safe_filename(test_name)}.log"
    filepath = os.path.join(session_dir, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        if order is not None:
            f.write(f"Order: {order}\n")
        f.write(f"Test: {test_name}\n")
        f.write(f"Command: {cmd}\n")
        f.write(f"Timestamp: {datetime.now().isoformat()}\n")
        f.write("=" * 60 + "\n")
        f.write("串口原文（含提示符与回显，可与手动 starry:~# 对照）\n")
        f.write("=" * 60 + "\n")
        f.write((raw_transcript if raw_transcript is not None else output).rstrip())
        f.write("\n\n")
        f.write("=" * 60 + "\n")
        f.write("用于子串断言的处理后输出（send_cmd 去重首行等）\n")
        f.write("=" * 60 + "\n")
        f.write(output.rstrip())
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
    logger.info(
        "Between tests: recover_shell() (leave stuck foreground jobs) then TEST['clean'] if set"
    )
    passed = 0
    failed = 0
    for test in tests:
        ord_n = runnable_order(test)
        ord_tag = f"[order {ord_n}] " if ord_n is not None else ""
        logger.info(f"Running test: {ord_tag}{test.name} -> {test.cmd}")
        client.begin_test_capture()
        ok, msg, output = test.run(client)
        raw_ts = client.get_serial_transcript_for_log()
        save_output_to_file(
            test.cmd,
            output,
            test.name,
            session_dir,
            raw_transcript=raw_ts,
            order=ord_n,
        )
        client.begin_test_capture()
        if ok:
            logger.info(f"✅ PASS: {ord_tag}{test.name} - {msg}")
            passed += 1
        else:
            logger.error(f"❌ FAIL: {ord_tag}{test.name} - {msg}")
            failed += 1
        client.recover_shell()
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
        order_range=args.order_range,
        orders=args.orders,
    )
    filtered = (
        args.test_name is not None
        or args.order is not None
        or args.order_range is not None
        or args.orders is not None
    )
    if filtered:
        if not suite:
            logger.error(
                "No test matches the filter (--test / --order / --order-range / --orders). "
                "Check busybox/test_*.py TEST['name'] and TEST['order']."
            )
            _detach_session_report_log(report_fh)
            sys.exit(1)
        if args.order_range is not None:
            lo, hi = args.order_range
            logger.info(
                f"Order-range mode: {lo}-{hi} (inclusive), name={args.test_name!r} "
                f"-> {len(suite)} case(s)"
            )
        elif args.orders is not None:
            logger.info(
                f"Orders list mode: {list(args.orders)}, name={args.test_name!r} "
                f"-> {len(suite)} case(s)"
            )
        else:
            logger.info(
                f"Single-test mode: name={args.test_name!r} order={args.order!r} "
                f"-> {len(suite)} case(s)"
            )
    if not suite:
        logger.warning("No tests discovered under busybox/; add busybox/test_*.py with TEST dict.")
    client = QemuSerialClient(host=SERIAL_HOST, port=4444, timeout=1.0)
    try:
        client.connect()
        client.recover_shell()
        if not client.probe_serial_forwards_stdout():
            logger.warning(
                "当前 TCP 串口似乎未转发命令的标准输出（busybox id 未见 uid=/gid=）。"
                "若你在 starry:~# 手动能跑通而本脚本始终只有「.busybox…」式回显，"
                "请核对 QEMU -serial 是否指向与手动终端相同的一路（pty/telnet/tcp 等）；"
                "若刚跑过会占前台的 applet（如 acpid），可先被 recover_shell 打断后再测。"
                "在仅回显、无 stdout 时，依赖子串的用例（如 base64）无法通过。"
            )
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
