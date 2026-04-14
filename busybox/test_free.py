# free：内存信息

TEST = {
    "order": 79,
    "name": "busybox_free",
    "cmd": "busybox free 2>&1",
    "expected_substring": "Mem",
    "expect_non_empty": True,
    "timeout": 2.0,
}
