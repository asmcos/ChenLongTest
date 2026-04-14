# lsmod：已加载模块列表

TEST = {
    "order": 137,
    "name": "busybox_lsmod",
    "cmd": "busybox lsmod 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 2.0,
}
