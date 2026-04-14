# tty：当前终端设备名

TEST = {
    "order": 267,
    "name": "busybox_tty",
    "cmd": "busybox tty 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 2.0,
}
