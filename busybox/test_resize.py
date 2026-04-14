# resize：无真实 tty 时多为错误；仅看帮助

TEST = {
    "order": 211,
    "name": "busybox_resize",
    "cmd": "busybox resize -h 2>&1",
    "expected_substring": "Usage",
    "expect_non_empty": True,
    "timeout": 2.0,
}
