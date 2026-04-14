# ifconfig：网卡列表（无网卡时也可能只有提示）

TEST = {
    "order": 98,
    "name": "busybox_ifconfig",
    "cmd": "busybox ifconfig -a 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 2.0,
}
