# busybox_list.log：dos2unix 之后 — du

TEST = {
    "order": 57,
    "name": "busybox_du",
    "cmd": "busybox du -s / 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 3.0,
}
