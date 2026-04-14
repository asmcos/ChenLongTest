# nbd-client：无服务器时连接会失败；仅看帮助

TEST = {
    "order": 167,
    "name": "busybox_nbd_client",
    "cmd": "busybox nbd-client -h 2>&1",
    "expected_substring": "Usage",
    "expect_non_empty": True,
    "timeout": 2.0,
}
