# fdflush：帮助输出（避免依赖软驱/设备环境）

TEST = {
    "order": 72,
    "name": "busybox_fdflush",
    "cmd": "busybox fdflush -h 2>&1",
    "expected_substring": "Usage: fdflush",
    "expect_non_empty": True,
    "timeout": 2.0,
}
