# swapon：危险，仅校验帮助

TEST = {
    "order": 247,
    "name": "busybox_swapon",
    "cmd": "busybox swapon -h 2>&1",
    "expected_substring": "Usage: swapon",
    "expect_non_empty": True,
    "timeout": 2.0,
}
