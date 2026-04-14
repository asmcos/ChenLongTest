# setpriv：仅看帮助

TEST = {
    "order": 226,
    "name": "busybox_setpriv",
    "cmd": "busybox setpriv -h 2>&1",
    "expected_substring": "Usage: setpriv",
    "expect_non_empty": True,
    "timeout": 2.0,
}
