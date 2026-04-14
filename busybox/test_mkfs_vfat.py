# mkfs.vfat：勿对真实块设备格式化；仅看帮助

TEST = {
    "order": 152,
    "name": "busybox_mkfs_vfat",
    "cmd": "busybox mkfs.vfat -h 2>&1",
    "expected_substring": "Usage",
    "expect_non_empty": True,
    "timeout": 2.0,
}
