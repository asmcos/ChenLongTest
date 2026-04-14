# pidof：查找 init 的 pid

TEST = {
    "order": 185,
    "name": "busybox_pidof",
    "cmd": "busybox pidof init 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 2.0,
}
