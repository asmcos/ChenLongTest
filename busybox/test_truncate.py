# truncate：截断文件长度

TEST = {
    "order": 266,
    "name": "busybox_truncate",
    "cmd": "busybox sh -c 'busybox echo abcd > /tmp/bb_trunc_f && busybox truncate -s 2 /tmp/bb_trunc_f && busybox cat /tmp/bb_trunc_f' 2>&1",
    "expected_substring": "ab",
    "expect_non_empty": True,
    "clean": "busybox rm -f /tmp/bb_trunc_f",
    "timeout": 2.0,
}
