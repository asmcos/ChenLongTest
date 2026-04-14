# sleep：零秒睡眠后继续

TEST = {
    "order": 238,
    "name": "busybox_sleep",
    "cmd": "busybox sleep 0 && busybox echo sleep_ok 2>&1",
    "expected_substring": "sleep_ok",
    "expect_non_empty": True,
    "timeout": 3.0,
}
