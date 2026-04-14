# reboot：仅看帮助，勿真重启

TEST = {
    "order": 206,
    "name": "busybox_reboot",
    "cmd": "busybox reboot -h 2>&1",
    "expected_substring": "Usage: reboot",
    "expect_non_empty": True,
    "timeout": 2.0,
}
