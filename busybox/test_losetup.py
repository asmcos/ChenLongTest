# losetup：查看 loop 设备

TEST = {
    "order": 134,
    "name": "busybox_losetup",
    "cmd": "busybox losetup -a 2>&1; busybox echo losetup_ok",
    "expected_substring": "losetup_ok",
    "expect_non_empty": True,
    "timeout": 2.0,
}
