# busybox_list.log：cal 之后 — cat

TEST = {
    "order": 26,
    "name": "busybox_cat",
    "cmd": "busybox cat /proc/version 2>&1",
    "expected_substring": "Linux",
    "expect_non_empty": True,
    "timeout": 2.0,
}
