# unzip：解压 zip，仅校验帮助

TEST = {
    "order": 282,
    "name": "busybox_unzip",
    "cmd": "busybox unzip -h 2>&1",
    "expected_substring": "Usage",
    "expect_non_empty": True,
    "timeout": 2.0,
}
