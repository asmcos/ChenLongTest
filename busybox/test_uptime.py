# uptime：运行时间与负载

TEST = {
    "order": 283,
    "name": "busybox_uptime",
    "cmd": "busybox uptime 2>&1; busybox echo uptime_ok",
    "expected_substring": "uptime_ok",
    "expect_non_empty": True,
    "timeout": 2.0,
}
