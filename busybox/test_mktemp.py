# mktemp：创建临时目录并打印路径

TEST = {
    "order": 156,
    "name": "busybox_mktemp",
    "cmd": "busybox sh -c 'd=$(busybox mktemp -d -t bbXXXXXX) && busybox test -d "$d" && busybox echo mktemp_ok && busybox rm -rf "$d"' 2>&1",
    "expected_substring": "mktemp_ok",
    "expect_non_empty": True,
    "timeout": 2.0,
}
