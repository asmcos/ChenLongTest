# factor：分解质因数

TEST = {
    "order": 66,
    "name": "busybox_factor",
    "cmd": "busybox factor 6 2>&1",
    "expected_substring": "6: 2 3",
    "expect_non_empty": True,
    "timeout": 2.0,
}
