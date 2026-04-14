# mdev：设备节点管理（仅看帮助，避免误创设备）

TEST = {
    "order": 146,
    "name": "busybox_mdev",
    "cmd": "busybox mdev -h 2>&1",
    "expected_substring": "Usage",
    "expect_non_empty": True,
    "timeout": 2.0,
}
