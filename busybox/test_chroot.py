# busybox_list.log：chpasswd 之后 — chroot

TEST = {
    "order": 32,
    "name": "busybox_chroot",
    "cmd": "busybox chroot -h 2>&1",
    "expected_substring": "Usage",
    "expect_non_empty": True,
    "timeout": 2.0,
}
