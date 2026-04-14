# timeout：限时执行子命令

TEST = {
    "order": 258,
    "name": "busybox_timeout",
    "cmd": "busybox timeout 2 busybox echo timeout_ok 2>&1",
    "expected_substring": "timeout_ok",
    "expect_non_empty": True,
    "timeout": 4.0,
}
