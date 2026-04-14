# swapoff：危险，仅校验帮助

TEST = {
    "order": 246,
    "name": "busybox_swapoff",
    "cmd": "busybox swapoff -h 2>&1",
    "expected_substring": "Usage: swapoff",
    "expect_non_empty": True,
    "timeout": 2.0,
}
