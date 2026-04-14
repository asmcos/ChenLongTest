# fsck：仅看版本信息（避免触碰真实分区）

TEST = {
    "order": 80,
    "name": "busybox_fsck",
    "cmd": "busybox fsck -V 2>&1",
    "expected_substring": "fsck",
    "expect_non_empty": True,
    "timeout": 2.0,
}
