# slattach：串口线路规程，无 tty 时仅校验帮助

TEST = {
    "order": 237,
    "name": "busybox_slattach",
    "cmd": "busybox slattach -h 2>&1",
    "expected_substring": "Usage",
    "expect_non_empty": True,
    "timeout": 2.0,
}
