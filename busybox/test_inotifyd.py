# inotifyd：帮助输出

TEST = {
    "order": 103,
    "name": "busybox_inotifyd",
    "cmd": "busybox inotifyd -h 2>&1",
    "expected_substring": "Usage: inotifyd",
    "expect_non_empty": True,
    "timeout": 2.0,
}
