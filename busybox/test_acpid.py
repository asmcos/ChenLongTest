# busybox --list 中第 1 个 applet：acpid

TEST = {
    "order": 1,
    "name": "busybox_acpid",
    "cmd": "busybox acpid 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 2.0,
}
