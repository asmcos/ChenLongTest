# busybox_list.log：brctl 之后 — bunzip2

TEST = {
    "order": 22,
    "name": "busybox_bunzip2",
    "cmd": "busybox bunzip2 -h 2>&1",
    "expected_substring": "Usage",
    "expect_non_empty": True,
    "timeout": 2.0,
}
