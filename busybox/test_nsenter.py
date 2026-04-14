# nsenter：仅看帮助，勿随意进其它命名空间

TEST = {
    "order": 176,
    "name": "busybox_nsenter",
    "cmd": "busybox nsenter -h 2>&1",
    "expected_substring": "Usage: nsenter",
    "expect_non_empty": True,
    "timeout": 2.0,
}
