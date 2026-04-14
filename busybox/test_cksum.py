# busybox_list.log：chvt 之后 — cksum

TEST = {
    "order": 34,
    "name": "busybox_cksum",
    "cmd": "busybox cksum /proc/version 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 2.0,
}
