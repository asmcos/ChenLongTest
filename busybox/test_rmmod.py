# rmmod：仅看帮助，勿卸载正在用的模块

TEST = {
    "order": 216,
    "name": "busybox_rmmod",
    "cmd": "busybox rmmod -h 2>&1",
    "expected_substring": "Usage: rmmod",
    "expect_non_empty": True,
    "timeout": 2.0,
}
