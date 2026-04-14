# whoami：当前有效用户

TEST = {
    "order": 297,
    "name": "busybox_whoami",
    "cmd": "busybox whoami 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 2.0,
}
