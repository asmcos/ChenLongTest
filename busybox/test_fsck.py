# fsck：不对真实分区做检查；仅看版本/帮助类输出（避免误伤数据）

TEST = {
    "order": 80,
    "name": "busybox_fsck",
    "cmd": "busybox fsck -V 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 2.0,
}
