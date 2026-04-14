# ipneigh：邻居表

TEST = {
    "order": 114,
    "name": "busybox_ipneigh",
    "cmd": "busybox ip neigh show 2>&1; busybox echo ipneigh_ok",
    "expected_substring": "ipneigh_ok",
    "expect_non_empty": True,
    "timeout": 2.0,
}
