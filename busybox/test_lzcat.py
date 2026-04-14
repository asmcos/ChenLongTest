# lzcat：解压 lzma 流（echo test | lzma -c | lzcat）

TEST = {
    "order": 140,
    "name": "busybox_lzcat",
    "cmd": "busybox echo -n test | busybox lzma -c 2>/dev/null | busybox lzcat 2>&1",
    "expected_substring": "test",
    "expect_non_empty": True,
    "timeout": 3.0,
}
