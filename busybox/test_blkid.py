# busybox_list.log：blkdiscard 之后 — blkid
#
# Starry 上对 /dev/null 可能只打内核 ioctl 日志、不出现路径字符串；其它环境可能有
# blkid 报错行或 Usage。用 run() 接受多种稳定片段。

from __future__ import annotations

from typing import Tuple

from harness import QemuSerialClient

_CMD = "busybox blkid /dev/null 2>&1"
_MARKERS = (
    "/dev/null",
    "Usage:",
    "Usage: blkid",
    "not a block",
    "No such file",
    "Unsupported ioctl",
)


def run(client: QemuSerialClient) -> Tuple[bool, str, str]:
    out = client.send_cmd(_CMD, timeout=2.0)
    if any(m in out for m in _MARKERS):
        return True, "blkid: matched expected error/trace/usage fragment", out
    return (
        False,
        f"Unexpected blkid output (no known marker). Preview: {out[:200]!r}",
        out,
    )


TEST = {
    "order": 19,
    "name": "busybox_blkid",
    "cmd": _CMD,
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 2.0,
}
