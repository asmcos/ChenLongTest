# hd：十六进制查看

TEST = {
    "order": 91,
    "name": "busybox_hd",
    "cmd": "busybox hd -n 64 /proc/version 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 2.0,
}
