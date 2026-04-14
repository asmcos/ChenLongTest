# unlink：删除文件（同 unlink(2)）

TEST = {
    "order": 277,
    "name": "busybox_unlink",
    "cmd": "busybox sh -c 'busybox echo u > /tmp/bb_unl && busybox unlink /tmp/bb_unl && busybox test ! -e /tmp/bb_unl && busybox echo unlink_ok' 2>&1",
    "expected_substring": "unlink_ok",
    "expect_non_empty": True,
    "timeout": 2.0,
}
