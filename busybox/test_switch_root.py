# switch_root：危险，仅校验帮助

TEST = {
    "order": 248,
    "name": "busybox_switch_root",
    "cmd": "busybox switch_root -h 2>&1",
    "expected_substring": "Usage: switch_root",
    "expect_non_empty": True,
    "timeout": 2.0,
}
