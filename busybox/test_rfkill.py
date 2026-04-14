# rfkill：无线开关列表（无设备时也可能只有表头）

TEST = {
    "order": 213,
    "name": "busybox_rfkill",
    "cmd": "busybox rfkill list 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 2.0,
}
