# busybox_list.log：beep 之后 — blkdiscard（真实功能校验）
#
# 目标：在可用块设备上执行 discard，并检查退出码为 0。
# 当前 Starry/QEMU 若设备或 ioctl 不支持，应 FAIL（暴露能力缺口，而非误判 PASS）。

from __future__ import annotations

from typing import Tuple

from harness import QemuSerialClient

_CMD = "busybox blkdiscard /dev/loop0 2>&1; busybox echo __RC:$?"


def run(client: QemuSerialClient) -> Tuple[bool, str, str]:
    out = client.send_cmd(_CMD, timeout=3.0)
    if "__RC:0" in out:
        return True, "blkdiscard succeeded on /dev/loop0 (__RC:0)", out
    return (
        False,
        "blkdiscard failed or unsupported on /dev/loop0 (expected __RC:0)",
        out,
    )


TEST = {
    "order": 18,
    "name": "busybox_blkdiscard",
    "cmd": _CMD,
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 3.0,
}
