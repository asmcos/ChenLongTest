# ipaddr：改用更通用子命令 ip addr

TEST = {
    "order": 109,
    "name": "busybox_ipaddr",
    "cmd": "busybox ip addr 2>&1",
    "expected_substring": "inet",
    "expect_non_empty": True,
    "timeout": 2.0,
}
