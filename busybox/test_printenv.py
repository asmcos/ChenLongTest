# printenv：打印 PATH

TEST = {
    "order": 193,
    "name": "busybox_printenv",
    "cmd": "busybox printenv PATH 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 2.0,
}
