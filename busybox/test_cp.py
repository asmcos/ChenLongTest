# busybox_list.log：comm 之后 — cp

TEST = {
    "order": 38,
    "name": "busybox_cp",
    "cmd": "busybox cp -h 2>&1",
    "expected_substring": "Usage",
    "expect_non_empty": True,
    "timeout": 2.0,
}
