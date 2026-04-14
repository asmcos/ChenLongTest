# iplink：等价于 ip link 一类输出

TEST = {
    "order": 113,
    "name": "busybox_iplink",
    "cmd": "busybox iplink 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 2.0,
}
