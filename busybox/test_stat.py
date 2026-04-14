# stat：文件状态

TEST = {
    "order": 241,
    "name": "busybox_stat",
    "cmd": "busybox stat /proc/version 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 2.0,
}
