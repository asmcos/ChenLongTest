# umount：卸载文件系统，仅校验帮助

TEST = {
    "order": 272,
    "name": "busybox_umount",
    "cmd": "busybox umount -h 2>&1",
    "expected_substring": "Usage",
    "expect_non_empty": True,
    "timeout": 2.0,
}
