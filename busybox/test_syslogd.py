# syslogd：后台守护进程，仅校验帮助

TEST = {
    "order": 251,
    "name": "busybox_syslogd",
    "cmd": "busybox syslogd -h 2>&1",
    "expected_substring": "Usage: syslogd",
    "expect_non_empty": True,
    "timeout": 2.0,
}
