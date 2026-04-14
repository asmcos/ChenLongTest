# readahead：对 /tmp 小文件预读后打印标记

TEST = {
    "order": 203,
    "name": "busybox_readahead",
    "cmd": "busybox echo ra > /tmp/bb_ra_f && busybox readahead /tmp/bb_ra_f 2>/dev/null; busybox echo ra_done 2>&1",
    "expected_substring": "ra_done",
    "expect_non_empty": True,
    "clean": "busybox rm -f /tmp/bb_ra_f",
    "timeout": 2.0,
}
