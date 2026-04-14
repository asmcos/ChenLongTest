# pwd：当前目录

TEST = {
    "order": 198,
    "name": "busybox_pwd",
    "cmd": "busybox pwd 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 2.0,
}
