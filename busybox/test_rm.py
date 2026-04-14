# rm：删除 /tmp 文件后确认不存在

TEST = {
    "order": 214,
    "name": "busybox_rm",
    "cmd": "busybox sh -c 'busybox touch /tmp/bb_rm_x && busybox rm /tmp/bb_rm_x && busybox test ! -e /tmp/bb_rm_x && busybox echo rm_ok' 2>&1",
    "expected_substring": "rm_ok",
    "expect_non_empty": True,
    "timeout": 2.0,
}
