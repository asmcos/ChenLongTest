# traceroute6：需网络/特权，仅校验帮助

TEST = {
    "order": 263,
    "name": "busybox_traceroute6",
    "cmd": "busybox traceroute6 -h 2>&1",
    "expected_substring": "Usage: traceroute6",
    "expect_non_empty": True,
    "timeout": 2.0,
}
