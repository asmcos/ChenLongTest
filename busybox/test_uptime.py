# uptime：运行时间与负载

TEST = {
    "order": 283,
    "name": "busybox_uptime",
    "cmd": "busybox uptime 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 2.0,
}
