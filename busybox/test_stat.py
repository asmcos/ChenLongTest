# stat：文件状态

TEST = {
    "order": 241,
    "name": "busybox_stat",
    "cmd": "busybox stat /etc/passwd 2>&1",
    "expected_substring": "File: /etc/passwd",
    "expect_non_empty": True,
    "timeout": 2.0,
}
