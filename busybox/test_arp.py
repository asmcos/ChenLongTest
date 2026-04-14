# arp：当前镜像无 /proc/net/arp，预期返回缺失提示

TEST = {
    "order": 9,
    "name": "busybox_arp",
    "cmd": "busybox arp 2>&1",
    "expected_substring": "/proc/net/arp",
    "expect_non_empty": True,
    "timeout": 2.0,
}
