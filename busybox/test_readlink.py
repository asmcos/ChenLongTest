# readlink：解析 /proc/self/exe

TEST = {
    "order": 204,
    "name": "busybox_readlink",
    "cmd": "busybox readlink -f /proc/self/exe 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 2.0,
}
