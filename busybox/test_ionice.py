# ionice：帮助输出（避免影响当前进程调度）

TEST = {
    "order": 106,
    "name": "busybox_ionice",
    "cmd": "busybox ionice -h 2>&1",
    "expected_substring": "Usage: ionice",
    "expect_non_empty": True,
    "timeout": 2.0,
}
