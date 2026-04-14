# which：查找可执行路径

TEST = {
    "order": 295,
    "name": "busybox_which",
    "cmd": "busybox which busybox 2>&1",
    "expected_substring": "busybox",
    "expect_non_empty": True,
    "timeout": 2.0,
}
