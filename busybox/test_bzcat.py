# busybox_list.log：bunzip2 之后 — bzcat

TEST = {
    "order": 23,
    "name": "busybox_bzcat",
    "cmd": "busybox bzcat -h 2>&1",
    "expected_substring": "Usage",
    "expect_non_empty": True,
    "timeout": 2.0,
}
