# watchdog：看门狗守护进程，仅校验帮助

TEST = {
    "order": 292,
    "name": "busybox_watchdog",
    "cmd": "busybox watchdog -h 2>&1",
    "expected_substring": "Usage: watchdog",
    "expect_non_empty": True,
    "timeout": 2.0,
}
