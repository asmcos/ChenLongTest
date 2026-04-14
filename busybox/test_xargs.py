# xargs：从 stdin 拼参数

TEST = {
    "order": 299,
    "name": "busybox_xargs",
    "cmd": "busybox echo a b | busybox xargs busybox echo X 2>&1",
    "expected_substring": "X a b",
    "expect_non_empty": True,
    "timeout": 2.0,
}
