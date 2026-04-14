# lzop：压缩 stdout

TEST = {
    "order": 142,
    "name": "busybox_lzop",
    "cmd": "busybox echo -n lzop_t | busybox lzop -c 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 2.0,
}
