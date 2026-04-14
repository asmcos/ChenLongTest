# busybox_list.log：chown 之后 — chpasswd

TEST = {
    "order": 31,
    "name": "busybox_chpasswd",
    "cmd": "busybox chpasswd -h 2>&1",
    "expected_substring": "Usage: chpasswd",
    "expect_non_empty": True,
    "timeout": 2.0,
}
