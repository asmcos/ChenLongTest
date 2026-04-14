# mountpoint：根是否挂载点

TEST = {
    "order": 161,
    "name": "busybox_mountpoint",
    "cmd": "busybox mountpoint / 2>&1",
    "expected_substring": "is a mountpoint",
    "expect_non_empty": True,
    "timeout": 2.0,
}
