# pscan：端口扫描（无目标时多为用法）

TEST = {
    "order": 196,
    "name": "busybox_pscan",
    "cmd": "busybox pscan 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 2.0,
}
