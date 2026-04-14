# busybox_list.log：cpio 之后 — crond

TEST = {
    "order": 40,
    "name": "busybox_crond",
    "cmd": "busybox crond -h 2>&1",
    "expected_substring": "Usage: crond",
    "expect_non_empty": True,
    "timeout": 2.0,
}
