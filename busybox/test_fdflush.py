# fdflush：无软驱时多为错误信息

TEST = {
    "order": 72,
    "name": "busybox_fdflush",
    "cmd": "busybox fdflush 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 2.0,
}
