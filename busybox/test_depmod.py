# busybox_list.log：deluser 之后 — depmod

TEST = {
    "order": 50,
    "name": "busybox_depmod",
    "cmd": "busybox depmod -h 2>&1",
    "expected_substring": "Usage: depmod",
    "expect_non_empty": True,
    "timeout": 2.0,
}
