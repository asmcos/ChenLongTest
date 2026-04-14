# ipneigh：邻居表

TEST = {
    "order": 114,
    "name": "busybox_ipneigh",
    "cmd": "busybox ipneigh 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 2.0,
}
