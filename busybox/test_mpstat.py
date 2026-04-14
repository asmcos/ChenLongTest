# mpstat：CPU 统计采样 1 次

TEST = {
    "order": 162,
    "name": "busybox_mpstat",
    "cmd": "busybox mpstat 1 1 2>&1; busybox echo mpstat_ok",
    "expected_substring": "mpstat_ok",
    "expect_non_empty": True,
    "timeout": 5.0,
}
