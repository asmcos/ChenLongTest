# unshare：命名空间隔离，仅校验帮助

TEST = {
    "order": 280,
    "name": "busybox_unshare",
    "cmd": "busybox unshare -h 2>&1",
    "expected_substring": "Usage: unshare",
    "expect_non_empty": True,
    "timeout": 2.0,
}
