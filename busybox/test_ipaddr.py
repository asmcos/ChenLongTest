# ipaddr：BusyBox 多调用名；失败可改为 ip addr show

TEST = {
    "order": 109,
    "name": "busybox_ipaddr",
    "cmd": "busybox ipaddr 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 2.0,
}
