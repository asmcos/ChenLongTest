# setfont：仅看帮助

TEST = {
    "order": 223,
    "name": "busybox_setfont",
    "cmd": "busybox setfont -h 2>&1",
    "expected_substring": "Usage",
    "expect_non_empty": True,
    "timeout": 2.0,
}
