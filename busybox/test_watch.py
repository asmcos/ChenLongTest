# watch：周期性执行命令，仅校验帮助（避免常驻）

TEST = {
    "order": 291,
    "name": "busybox_watch",
    "cmd": "busybox watch -h 2>&1",
    "expected_substring": "Usage",
    "expect_non_empty": True,
    "timeout": 2.0,
}
