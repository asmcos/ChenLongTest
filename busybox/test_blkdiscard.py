# busybox_list.log：beep 之后 — blkdiscard
#
# 不再用「无参看 Usage」；改为对 /dev/null 执行真实丢弃动作，
# 在 QEMU/Starry 环境通常会走设备错误或 ioctl 错误路径。

from __future__ import annotations

from typing import Tuple

from harness import QemuSerialClient

_CMD = "busybox blkdiscard /dev/null 2>&1"
_MARKERS = (
    "/dev/null",
    "not a block",
    "Operation not supported",
    "Inappropriate ioctl",
    "Unsupported ioctl",
    "No such file",
)


def run(client: QemuSerialClient) -> Tuple[bool, str, str]:
    out = client.send_cmd(_CMD, timeout=2.0)
    if any(m in out for m in _MARKERS):
        return True, "blkdiscard: matched expected device-error/ioctl fragment", out
    return (
        False,
        f"Unexpected blkdiscard output (no known marker). Preview: {out[:200]!r}",
        out,
    )


TEST = {
    "order": 18,
    "name": "busybox_blkdiscard",
    "cmd": _CMD,
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 2.0,
}
