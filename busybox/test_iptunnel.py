# iptunnel：隧道接口

TEST = {
    "order": 117,
    "name": "busybox_iptunnel",
    "cmd": "busybox iptunnel 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 2.0,
}
