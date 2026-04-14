# hexdump：管道十六进制

TEST = {
    "order": 93,
    "name": "busybox_hexdump",
    "cmd": "busybox echo -n ab | busybox hexdump -C 2>&1",
    "expected_substring": "61",
    "expect_non_empty": True,
    "timeout": 2.0,
}
