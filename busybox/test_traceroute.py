# traceroute：需网络/特权，仅校验帮助

TEST = {
    "order": 262,
    "name": "busybox_traceroute",
    "cmd": "busybox traceroute -h 2>&1",
    "expected_substring": "Usage",
    "expect_non_empty": True,
    "timeout": 2.0,
}
