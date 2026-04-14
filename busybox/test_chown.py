# busybox_list.log：chmod 之后 — chown

TEST = {
    "order": 30,
    "name": "busybox_chown",
    "cmd": "busybox chown -h 2>&1",
    "expected_substring": "Usage",
    "expect_non_empty": True,
    "timeout": 2.0,
}
