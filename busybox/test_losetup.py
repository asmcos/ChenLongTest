# losetup：查看 loop 设备

TEST = {
    "order": 134,
    "name": "busybox_losetup",
    "cmd": "busybox losetup -a 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 2.0,
}
