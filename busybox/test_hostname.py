# hostname：打印主机名

TEST = {
    "order": 95,
    "name": "busybox_hostname",
    "cmd": "busybox hostname 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 2.0,
}
