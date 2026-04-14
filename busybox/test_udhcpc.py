# udhcpc：DHCP 客户端，仅校验帮助

TEST = {
    "order": 270,
    "name": "busybox_udhcpc",
    "cmd": "busybox udhcpc -h 2>&1",
    "expected_substring": "Usage",
    "expect_non_empty": True,
    "timeout": 2.0,
}
