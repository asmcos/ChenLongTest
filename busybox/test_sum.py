# sum：SysV 校验和

TEST = {
    "order": 245,
    "name": "busybox_sum",
    "cmd": "busybox echo sum_t | busybox sum 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 2.0,
}
