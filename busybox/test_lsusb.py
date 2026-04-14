# lsusb：USB 设备（无 USB 时也可能只有表头或提示）

TEST = {
    "order": 139,
    "name": "busybox_lsusb",
    "cmd": "busybox lsusb 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 2.0,
}
