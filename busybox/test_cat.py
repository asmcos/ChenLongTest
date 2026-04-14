# busybox_list.log：cal 之后 — cat

TEST = {
    "order": 26,
    "name": "busybox_cat",
    "cmd": "busybox cat /etc/passwd 2>&1",
    "expected_substring": "root:",
    "expect_non_empty": True,
    "timeout": 2.0,
}
