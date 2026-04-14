# du：统计当前目录，避免扫描 / 或依赖 /tmp 可写

TEST = {
    "order": 57,
    "name": "busybox_du",
    "cmd": "busybox du -s . 2>&1",
    "expected_substring": ".",
    "expect_non_empty": True,
    "timeout": 3.0,
}
