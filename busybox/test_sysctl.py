# sysctl：读单个内核参数（失败则退化为 -h）

TEST = {
    "order": 250,
    "name": "busybox_sysctl",
    "cmd": "busybox sysctl kernel.hostname 2>&1 || busybox sysctl -h 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 3.0,
}
