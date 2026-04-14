# mkdosfs：勿对真实盘格式化；仅看帮助

TEST = {
    "order": 150,
    "name": "busybox_mkdosfs",
    "cmd": "busybox mkdosfs -h 2>&1",
    "expected_substring": "Usage: mkdosfs",
    "expect_non_empty": True,
    "timeout": 2.0,
}
