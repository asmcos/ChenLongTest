# uuencode：uu 编码

TEST = {
    "order": 286,
    "name": "busybox_uuencode",
    "cmd": "busybox echo enc | busybox uuencode out 2>&1",
    "expected_substring": "begin",
    "expect_non_empty": True,
    "timeout": 2.0,
}
