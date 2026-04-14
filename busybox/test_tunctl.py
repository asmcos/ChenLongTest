# tunctl：TUN/TAP，仅校验帮助

TEST = {
    "order": 269,
    "name": "busybox_tunctl",
    "cmd": "busybox tunctl -h 2>&1",
    "expected_substring": "Usage: tunctl",
    "expect_non_empty": True,
    "timeout": 2.0,
}
