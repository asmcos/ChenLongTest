# busybox_list.log：bzcat 之后 — bzip2

TEST = {
    "order": 24,
    "name": "busybox_bzip2",
    "cmd": "busybox bzip2 -h 2>&1",
    "expected_substring": "Usage",
    "expect_non_empty": True,
    "timeout": 2.0,
}
