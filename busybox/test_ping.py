# ping：本机回环 1 包

TEST = {
    "order": 186,
    "name": "busybox_ping",
    "cmd": "busybox ping -c 1 127.0.0.1 2>&1",
    "expected_substring": "1 packets transmitted",
    "expect_non_empty": True,
    "timeout": 5.0,
}
