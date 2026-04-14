# lzopcat：lzop 流解压

TEST = {
    "order": 143,
    "name": "busybox_lzopcat",
    "cmd": "busybox echo -n round | busybox lzop -c 2>/dev/null | busybox lzopcat 2>&1",
    "expected_substring": "round",
    "expect_non_empty": True,
    "timeout": 2.0,
}
