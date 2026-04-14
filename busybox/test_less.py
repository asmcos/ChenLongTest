# less：帮助输出更稳定，避免交互分页

TEST = {
    "order": 124,
    "name": "busybox_less",
    "cmd": "busybox less -h 2>&1",
    "expected_substring": "Usage: less",
    "expect_non_empty": True,
    "timeout": 2.0,
}
