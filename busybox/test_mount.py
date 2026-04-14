# mount：列出已挂载（或错误信息）

TEST = {
    "order": 160,
    "name": "busybox_mount",
    "cmd": "busybox mount 2>&1; busybox echo mount_ok",
    "expected_substring": "mount_ok",
    "expect_non_empty": True,
    "timeout": 2.0,
}
