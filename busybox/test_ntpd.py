# ntpd：仅看帮助，不启动守护进程

TEST = {
    "order": 178,
    "name": "busybox_ntpd",
    "cmd": "busybox ntpd -h 2>&1",
    "expected_substring": "Usage",
    "expect_non_empty": True,
    "timeout": 2.0,
}
