# passwd：勿交互改密；仅看帮助

TEST = {
    "order": 182,
    "name": "busybox_passwd",
    "cmd": "busybox passwd -h 2>&1",
    "expected_substring": "Usage",
    "expect_non_empty": True,
    "timeout": 2.0,
}
