# od：八进制/十六进制转储

TEST = {
    "order": 179,
    "name": "busybox_od",
    "cmd": "busybox echo test | busybox od -An -tx1 2>&1",
    "expected_substring": "74",
    "expect_non_empty": True,
    "timeout": 2.0,
}
