# paste：合并两行

TEST = {
    "order": 183,
    "name": "busybox_paste",
    "cmd": "busybox echo a > /tmp/bb_p1 && busybox echo b > /tmp/bb_p2 && busybox paste /tmp/bb_p1 /tmp/bb_p2 2>&1",
    "expected_substring": "a",
    "expect_non_empty": True,
    "timeout": 2.0,
}
