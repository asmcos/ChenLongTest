# uname：内核与机器信息

TEST = {
    "order": 273,
    "name": "busybox_uname",
    "cmd": "busybox uname -a 2>&1",
    "expected_substring": "Linux",
    "expect_non_empty": True,
    "timeout": 2.0,
}
