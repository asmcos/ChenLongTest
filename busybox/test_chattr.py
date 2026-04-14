# busybox_list.log：cat 之后 — chattr

TEST = {
    "order": 27,
    "name": "busybox_chattr",
    "cmd": "busybox chattr -h 2>&1",
    "expected_substring": "Usage",
    "expect_non_empty": True,
    "timeout": 2.0,
}
