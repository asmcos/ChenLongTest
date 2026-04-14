# iptunnel：隧道接口

TEST = {
    "order": 117,
    "name": "busybox_iptunnel",
    "cmd": "busybox ip tunnel show 2>&1; busybox echo iptunnel_ok",
    "expected_substring": "iptunnel_ok",
    "expect_non_empty": True,
    "timeout": 2.0,
}
