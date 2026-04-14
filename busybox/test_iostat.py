# iostat：磁盘/CPU 统计（采样 1 次）

TEST = {
    "order": 107,
    "name": "busybox_iostat",
    "cmd": "busybox iostat 1 1 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 5.0,
}
