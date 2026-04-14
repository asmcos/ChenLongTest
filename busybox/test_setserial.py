# setserial：仅看帮助

TEST = {
    "order": 227,
    "name": "busybox_setserial",
    "cmd": "busybox setserial -h 2>&1",
    "expected_substring": "Usage",
    "expect_non_empty": True,
    "timeout": 2.0,
}
