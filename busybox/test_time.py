# time：计时执行命令

TEST = {
    "order": 257,
    "name": "busybox_time",
    "cmd": "busybox time busybox echo time_ok 2>&1",
    "expected_substring": "time_ok",
    "expect_non_empty": True,
    "timeout": 4.0,
}
