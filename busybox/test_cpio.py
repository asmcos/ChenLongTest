# busybox_list.log：cp 之后 — cpio

TEST = {
    "order": 39,
    "name": "busybox_cpio",
    "cmd": "busybox cpio -h 2>&1",
    "expected_substring": "Usage",
    "expect_non_empty": True,
    "timeout": 2.0,
}
