# openvt：无虚拟终端时多为错误；仅看帮助

TEST = {
    "order": 180,
    "name": "busybox_openvt",
    "cmd": "busybox openvt -h 2>&1",
    "expected_substring": "Usage",
    "expect_non_empty": True,
    "timeout": 2.0,
}
