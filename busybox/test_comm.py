# busybox_list.log：cmp 之后 — comm

TEST = {
    "order": 37,
    "name": "busybox_comm",
    "cmd": "busybox comm -h 2>&1",
    "expected_substring": "Usage",
    "expect_non_empty": True,
    "timeout": 2.0,
}
