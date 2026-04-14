# unlzma：解压 .lzma，无现成文件时仅校验帮助

TEST = {
    "order": 278,
    "name": "busybox_unlzma",
    "cmd": "busybox unlzma -h 2>&1",
    "expected_substring": "Usage: unlzma",
    "expect_non_empty": True,
    "timeout": 2.0,
}
