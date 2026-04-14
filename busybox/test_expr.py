# expr：整数运算

TEST = {
    "order": 65,
    "name": "busybox_expr",
    "cmd": "busybox expr 3 '*' 4 2>&1",
    "expected_substring": "12",
    "expect_non_empty": True,
    "timeout": 2.0,
}
