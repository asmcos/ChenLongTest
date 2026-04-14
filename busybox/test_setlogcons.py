# setlogcons：仅看帮助

TEST = {
    "order": 225,
    "name": "busybox_setlogcons",
    "cmd": "busybox setlogcons -h 2>&1",
    "expected_substring": "Usage",
    "expect_non_empty": True,
    "timeout": 2.0,
}
