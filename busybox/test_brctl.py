# busybox_list.log：blockdev 之后 — brctl

TEST = {
    "order": 21,
    "name": "busybox_brctl",
    "cmd": "busybox brctl -h 2>&1",
    "expected_substring": "Usage",
    "expect_non_empty": True,
    "timeout": 2.0,
}
