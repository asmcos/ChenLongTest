# sendmail：仅看帮助，勿真发信

TEST = {
    "order": 220,
    "name": "busybox_sendmail",
    "cmd": "busybox sendmail -h 2>&1",
    "expected_substring": "Usage",
    "expect_non_empty": True,
    "timeout": 2.0,
}
