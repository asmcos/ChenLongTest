# head：读 /proc/version 首行

TEST = {
    "order": 92,
    "name": "busybox_head",
    "cmd": "busybox head -n 1 /proc/version 2>&1",
    "expected_substring": "Linux",
    "expect_non_empty": True,
    "timeout": 2.0,
}
