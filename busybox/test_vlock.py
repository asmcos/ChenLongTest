# vlock：虚拟控制台锁，仅校验帮助

TEST = {
    "order": 289,
    "name": "busybox_vlock",
    "cmd": "busybox vlock -h 2>&1",
    "expected_substring": "Usage: vlock",
    "expect_non_empty": True,
    "timeout": 2.0,
}
