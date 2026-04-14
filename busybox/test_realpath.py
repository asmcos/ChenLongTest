# realpath：规范路径

TEST = {
    "order": 205,
    "name": "busybox_realpath",
    "cmd": "busybox realpath /tmp 2>&1",
    "expected_substring": "tmp",
    "expect_non_empty": True,
    "timeout": 2.0,
}
