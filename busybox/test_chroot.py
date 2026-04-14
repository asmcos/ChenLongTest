# busybox_list.log：chpasswd 之后 — chroot

TEST = {
    "order": 32,
    "name": "busybox_chroot",
    "cmd": "busybox chroot / /bin/busybox echo chroot_ok 2>&1",
    "expected_substring": "chroot_ok",
    "expect_non_empty": True,
    "timeout": 3.0,
}
