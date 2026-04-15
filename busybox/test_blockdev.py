# busybox_list.log：blkid 之后 — blockdev（真实功能校验）
#
# 目标：读取块设备 sector size，检查退出码为 0 且输出为数字。
# 当前 Starry/QEMU 若 ioctl 不支持，应 FAIL（暴露能力缺口，而非误判 PASS）。

from __future__ import annotations

from typing import Tuple

from harness import QemuSerialClient

_CMD = "busybox blockdev --getss /dev/loop0 2>&1; busybox echo __RC:$?"


def run(client: QemuSerialClient) -> Tuple[bool, str, str]:
    out = client.send_cmd(_CMD, timeout=3.0)
    if "__RC:0" not in out:
        return (
            False,
            "blockdev --getss failed or unsupported on /dev/loop0 (expected __RC:0)",
            out,
        )

    lines = [ln.strip() for ln in out.splitlines() if ln.strip() and not ln.strip().startswith("starry:~#")]
    data_lines = [ln for ln in lines if not ln.startswith("__RC:")]
    has_numeric = any(ln.isdigit() for ln in data_lines)
    if has_numeric:
        return True, "blockdev --getss returned numeric sector size with __RC:0", out
    return False, "blockdev rc=0 but no numeric sector-size output found", out


TEST = {
    "order": 20,
    "name": "busybox_blockdev",
    "cmd": _CMD,
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 3.0,
}
