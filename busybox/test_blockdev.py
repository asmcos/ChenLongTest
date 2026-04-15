# busybox_list.log：blkid 之后 — blockdev
#
# 不再用 -h；改测真实子命令（读取 sector size）。在 /dev/null 上应触发
# 非块设备 / ioctl 相关错误，用于确认命令路径可达。

from __future__ import annotations

from typing import Tuple

from harness import QemuSerialClient

_CMD = "busybox blockdev --getss /dev/null 2>&1"
_MARKERS = (
    "/dev/null",
    "not a block",
    "Inappropriate ioctl",
    "Unsupported ioctl",
    "No such file",
)


def run(client: QemuSerialClient) -> Tuple[bool, str, str]:
    out = client.send_cmd(_CMD, timeout=2.0)
    if any(m in out for m in _MARKERS):
        return True, "blockdev: matched expected device-error/ioctl fragment", out
    return (
        False,
        f"Unexpected blockdev output (no known marker). Preview: {out[:200]!r}",
        out,
    )


TEST = {
    "order": 20,
    "name": "busybox_blockdev",
    "cmd": _CMD,
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 2.0,
}
