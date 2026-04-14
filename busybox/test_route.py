# route：路由表

TEST = {
    "order": 217,
    "name": "busybox_route",
    "cmd": "busybox route -n 2>&1; busybox echo route_ok",
    "expected_substring": "route_ok",
    "expect_non_empty": True,
    "timeout": 2.0,
}
