# iproute：路由表

TEST = {
    "order": 115,
    "name": "busybox_iproute",
    "cmd": "busybox iproute 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 2.0,
}
