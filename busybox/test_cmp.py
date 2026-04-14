# busybox_list.log：clear 之后 — cmp

TEST = {
    "order": 36,
    "name": "busybox_cmp",
    "cmd": "busybox cmp -h 2>&1",
    "expected_substring": "Usage",
    "expect_non_empty": True,
    "timeout": 2.0,
}
