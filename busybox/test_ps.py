# ps：进程列表

TEST = {
    "order": 195,
    "name": "busybox_ps",
    "cmd": "busybox ps 2>&1; busybox echo ps_ok",
    "expected_substring": "ps_ok",
    "expect_non_empty": True,
    "timeout": 2.0,
}
