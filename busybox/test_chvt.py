# busybox_list.log：chroot 之后 — chvt

TEST = {
    "order": 33,
    "name": "busybox_chvt",
    "cmd": "busybox chvt -h 2>&1",
    "expected_substring": "invalid number",
    "expect_non_empty": True,
    "timeout": 2.0,
}
