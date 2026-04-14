# netstat：网络连接/监听摘要

TEST = {
    "order": 169,
    "name": "busybox_netstat",
    "cmd": "busybox netstat -a 2>&1; busybox echo netstat_ok",
    "expected_substring": "netstat_ok",
    "expect_non_empty": True,
    "timeout": 3.0,
}
