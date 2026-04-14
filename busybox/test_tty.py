# tty：当前终端设备名

TEST = {
    "order": 267,
    "name": "busybox_tty",
    "cmd": "busybox tty 2>&1; busybox echo tty_ok",
    "expected_substring": "tty_ok",
    "expect_non_empty": True,
    "timeout": 2.0,
}
