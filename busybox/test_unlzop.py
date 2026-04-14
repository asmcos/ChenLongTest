# unlzop：解压 .lzo，仅校验帮助

TEST = {
    "order": 279,
    "name": "busybox_unlzop",
    "cmd": "busybox unlzop -h 2>&1",
    "expected_substring": "Usage",
    "expect_non_empty": True,
    "timeout": 2.0,
}
