# lzma：压缩 stdout

TEST = {
    "order": 141,
    "name": "busybox_lzma",
    "cmd": "busybox echo -n lzma_t | busybox lzma -c 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 2.0,
}
