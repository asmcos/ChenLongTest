# busybox_list.log：df 之后 — diff

TEST = {
    "order": 52,
    "name": "busybox_diff",
    "cmd": "busybox diff -h 2>&1",
    "expected_substring": "Usage",
    "expect_non_empty": True,
    "timeout": 2.0,
}
