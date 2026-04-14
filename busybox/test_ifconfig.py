# ifconfig：仅测帮助输出，避免依赖网卡拓扑

TEST = {
    "order": 98,
    "name": "busybox_ifconfig",
    "cmd": "busybox ifconfig -h 2>&1",
    "expected_substring": "Usage: ifconfig",
    "expect_non_empty": True,
    "timeout": 2.0,
}
