# fdisk：列出分区表（无权限时也会有错误输出）

TEST = {
    "order": 73,
    "name": "busybox_fdisk",
    "cmd": "busybox fdisk -l 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 3.0,
}
