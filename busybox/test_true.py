# true：恒真

TEST = {
    "order": 265,
    "name": "busybox_true",
    "cmd": "busybox true && busybox echo true_ok 2>&1",
    "expected_substring": "true_ok",
    "expect_non_empty": True,
    "timeout": 2.0,
}
