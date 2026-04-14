# busybox_list.log 中 adjtimex 之后第 1 个 applet：arch

TEST = {
    "order": 8,
    "name": "busybox_arch",
    "cmd": "busybox arch 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 2.0,
}
