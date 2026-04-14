# poweroff：仅看帮助，勿真关机

TEST = {
    "order": 192,
    "name": "busybox_poweroff",
    "cmd": "busybox poweroff -h 2>&1",
    "expected_substring": "Usage",
    "expect_non_empty": True,
    "timeout": 2.0,
}
