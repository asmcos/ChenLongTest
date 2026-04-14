# shred：覆写后删除临时文件

TEST = {
    "order": 235,
    "name": "busybox_shred",
    "cmd": "busybox sh -c 'echo x > /tmp/bb_shred_t && busybox shred -n 1 -u /tmp/bb_shred_t 2>&1; busybox test ! -f /tmp/bb_shred_t && busybox echo shred_ok' 2>&1",
    "expected_substring": "shred_ok",
    "expect_non_empty": True,
    "timeout": 5.0,
}
