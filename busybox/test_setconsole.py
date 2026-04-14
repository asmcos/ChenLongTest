# setconsole：仅看帮助

TEST = {
    "order": 222,
    "name": "busybox_setconsole",
    "cmd": "busybox setconsole -h 2>&1",
    "expected_substring": "Usage: setconsole",
    "expect_non_empty": True,
    "timeout": 2.0,
}
