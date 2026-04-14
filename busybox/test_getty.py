# getty：仅测帮助输出，避免无参进入设备等待

TEST = {
    "order": 85,
    "name": "busybox_getty",
    "cmd": "busybox getty -h 2>&1",
    "expected_substring": "Usage: getty",
    "expect_non_empty": True,
    "timeout": 2.0,
}
