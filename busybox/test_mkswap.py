# mkswap：勿对真实分区；仅看帮助

TEST = {
    "order": 155,
    "name": "busybox_mkswap",
    "cmd": "busybox mkswap -h 2>&1",
    "expected_substring": "Usage",
    "expect_non_empty": True,
    "timeout": 2.0,
}
