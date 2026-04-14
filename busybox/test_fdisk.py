# fdisk：帮助输出（避免对实际块设备做扫描）

TEST = {
    "order": 73,
    "name": "busybox_fdisk",
    "cmd": "busybox fdisk -h 2>&1",
    "expected_substring": "Usage: fdisk",
    "expect_non_empty": True,
    "timeout": 2.0,
}
