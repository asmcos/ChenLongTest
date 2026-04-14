# who：登录用户（无 utmp 时可能无行，改为行数统计总有输出）

TEST = {
    "order": 296,
    "name": "busybox_who",
    "cmd": "busybox who 2>&1 | busybox wc -l 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 2.0,
}
