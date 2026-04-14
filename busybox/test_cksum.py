# busybox_list.log：chvt 之后 — cksum

TEST = {
    "order": 34,
    "name": "busybox_cksum",
    "cmd": "busybox cksum /etc/passwd 2>&1",
    "expected_substring": "/etc/passwd",
    "expect_non_empty": True,
    "timeout": 2.0,
}
