# ifup：只测帮助输出，避免改动真实网络接口

TEST = {
    "order": 101,
    "name": "busybox_ifup",
    "cmd": "busybox ifup -h 2>&1",
    "expected_substring": "Usage: ifup",
    "expect_non_empty": True,
    "timeout": 2.0,
}
