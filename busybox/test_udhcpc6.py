# udhcpc6：DHCPv6 客户端，仅校验帮助

TEST = {
    "order": 271,
    "name": "busybox_udhcpc6",
    "cmd": "busybox udhcpc6 -h 2>&1",
    "expected_substring": "Usage",
    "expect_non_empty": True,
    "timeout": 2.0,
}
