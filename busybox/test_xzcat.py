# xzcat：解压 .xz 到 stdout，无现成文件时仅校验帮助

TEST = {
    "order": 301,
    "name": "busybox_xzcat",
    "cmd": "busybox xzcat -h 2>&1",
    "expected_substring": "Usage: xzcat",
    "expect_non_empty": True,
    "timeout": 2.0,
}
