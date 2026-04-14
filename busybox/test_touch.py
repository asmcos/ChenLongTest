# touch：创建空文件

TEST = {
    "order": 260,
    "name": "busybox_touch",
    "cmd": "busybox sh -c 'busybox touch /tmp/bb_touch_f && busybox test -f /tmp/bb_touch_f && busybox echo touch_ok' 2>&1",
    "expected_substring": "touch_ok",
    "expect_non_empty": True,
    "clean": "busybox rm -f /tmp/bb_touch_f",
    "timeout": 2.0,
}
