# route：路由表

TEST = {
    "order": 217,
    "name": "busybox_route",
    "cmd": "busybox route -n 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 2.0,
}
