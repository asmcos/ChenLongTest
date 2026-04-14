# ip：链路层信息（比 ifconfig 新）

TEST = {
    "order": 108,
    "name": "busybox_ip",
    "cmd": "busybox ip link 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 2.0,
}
