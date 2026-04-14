# usleep：微秒级睡眠

TEST = {
    "order": 284,
    "name": "busybox_usleep",
    "cmd": "busybox usleep 1 && busybox echo usleep_ok 2>&1",
    "expected_substring": "usleep_ok",
    "expect_non_empty": True,
    "timeout": 3.0,
}
