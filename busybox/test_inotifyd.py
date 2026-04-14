# inotifyd：无参时多为用法

TEST = {
    "order": 103,
    "name": "busybox_inotifyd",
    "cmd": "busybox inotifyd 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 2.0,
}
