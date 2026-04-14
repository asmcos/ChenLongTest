# fold：按宽度折行（每行 2 字符）

TEST = {
    "order": 78,
    "name": "busybox_fold",
    "cmd": "busybox echo abcdef | busybox fold -w 2 2>&1",
    "expected_substring": "ab",
    "expect_non_empty": True,
    "timeout": 2.0,
}
