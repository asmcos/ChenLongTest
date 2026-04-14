# busybox --list 中第 2 个 applet：add-shell

TEST = {
    "order": 2,
    "name": "busybox_add_shell",
    "cmd": "busybox add-shell 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 2.0,
}
