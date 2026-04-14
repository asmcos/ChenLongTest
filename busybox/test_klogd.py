# klogd：仅看帮助，不常驻读内核日志

TEST = {
    "order": 122,
    "name": "busybox_klogd",
    "cmd": "busybox klogd -h 2>&1",
    "expected_substring": "Usage: klogd",
    "expect_non_empty": True,
    "timeout": 2.0,
}
