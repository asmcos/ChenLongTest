# unxz：解压 .xz，仅校验帮助

TEST = {
    "order": 281,
    "name": "busybox_unxz",
    "cmd": "busybox unxz -h 2>&1",
    "expected_substring": "Usage",
    "expect_non_empty": True,
    "timeout": 2.0,
}
