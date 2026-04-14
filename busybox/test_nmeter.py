# nmeter：持续刷新会占串口；仅看帮助

TEST = {
    "order": 172,
    "name": "busybox_nmeter",
    "cmd": "busybox nmeter -h 2>&1",
    "expected_substring": "Usage",
    "expect_non_empty": True,
    "timeout": 2.0,
}
