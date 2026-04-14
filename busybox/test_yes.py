# yes：无限输出，用 head 截断一行

TEST = {
    "order": 302,
    "name": "busybox_yes",
    "cmd": "busybox yes y | busybox head -n 1 2>&1",
    "expected_substring": "y
",
    "expect_non_empty": True,
    "timeout": 3.0,
}
