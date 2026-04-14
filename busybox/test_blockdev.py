# busybox_list.log：blkid 之后 — blockdev

TEST = {
    "order": 20,
    "name": "busybox_blockdev",
    "cmd": "busybox blockdev -h 2>&1",
    "expected_substring": "Usage",
    "expect_non_empty": True,
    "timeout": 2.0,
}
