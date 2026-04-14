# grep：行匹配

TEST = {
    "order": 86,
    "name": "busybox_grep",
    "cmd": "busybox echo hello | busybox grep hell 2>&1",
    "expected_substring": "hello",
    "expect_non_empty": True,
    "timeout": 2.0,
}
