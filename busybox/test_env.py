# env：应至少输出形如 KEY=value 的行

TEST = {
    "order": 62,
    "name": "busybox_env",
    "cmd": "busybox env 2>&1",
    "expected_substring": "PATH=",
    "expect_non_empty": True,
    "timeout": 2.0,
}
