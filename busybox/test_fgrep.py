# fgrep：固定字符串匹配

TEST = {
    "order": 74,
    "name": "busybox_fgrep",
    "cmd": "busybox echo hello | busybox fgrep hell 2>&1",
    "expected_substring": "hello",
    "expect_non_empty": True,
    "timeout": 2.0,
}
