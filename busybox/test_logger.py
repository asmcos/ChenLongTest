# logger：写 syslog 常无 stdout；用 -h 校验帮助

TEST = {
    "order": 131,
    "name": "busybox_logger",
    "cmd": "busybox logger -h 2>&1",
    "expected_substring": "Usage: logger",
    "expect_non_empty": True,
    "timeout": 2.0,
}
