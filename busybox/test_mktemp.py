# mktemp：创建临时目录并打印路径

TEST = {
    "order": 156,
    "name": "busybox_mktemp",
    "cmd": "busybox mktemp -d -t bbXXXXXX 2>&1",
    "expected_substring": "bb",
    "expect_non_empty": True,
    "timeout": 2.0,
}
