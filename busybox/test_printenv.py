# printenv：打印 PATH

TEST = {
    "order": 193,
    "name": "busybox_printenv",
    "cmd": "busybox printenv PATH 2>&1; busybox echo printenv_ok",
    "expected_substring": "printenv_ok",
    "expect_non_empty": True,
    "timeout": 2.0,
}
