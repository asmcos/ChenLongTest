# busybox_list.log：dd 之后 — deallocvt

TEST = {
    "order": 47,
    "name": "busybox_deallocvt",
    "cmd": "busybox deallocvt -h 2>&1",
    "expected_substring": "invalid number",
    "expect_non_empty": True,
    "timeout": 2.0,
}
