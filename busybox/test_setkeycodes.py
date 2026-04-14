# setkeycodes：仅看帮助

TEST = {
    "order": 224,
    "name": "busybox_setkeycodes",
    "cmd": "busybox setkeycodes -h 2>&1",
    "expected_substring": "Usage",
    "expect_non_empty": True,
    "timeout": 2.0,
}
