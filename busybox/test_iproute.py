# iproute：路由表

TEST = {
    "order": 115,
    "name": "busybox_iproute",
    "cmd": "busybox ip route show 2>&1; busybox echo iproute_ok",
    "expected_substring": "iproute_ok",
    "expect_non_empty": True,
    "timeout": 2.0,
}
