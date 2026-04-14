# init：非 PID1 场景应拒绝执行，校验错误信息

TEST = {
    "order": 102,
    "name": "busybox_init",
    "cmd": "busybox init 2>&1",
    "expected_substring": "must be run as PID 1",
    "expect_non_empty": True,
    "timeout": 2.0,
}
