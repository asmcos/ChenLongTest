# mv：重命名 /tmp 文件并 cat

TEST = {
    "order": 163,
    "name": "busybox_mv",
    "cmd": "busybox echo mv_ok > /tmp/bb_mv_from && busybox mv /tmp/bb_mv_from /tmp/bb_mv_to && busybox cat /tmp/bb_mv_to 2>&1",
    "expected_substring": "mv_ok",
    "expect_non_empty": True,
    "timeout": 2.0,
}
