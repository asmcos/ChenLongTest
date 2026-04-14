# busybox --list 中第 5 个 applet：adjtimex

TEST = {
    "order": 5,
    "name": "busybox_adjtimex",
    "cmd": "busybox adjtimex 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 2.0,
}
