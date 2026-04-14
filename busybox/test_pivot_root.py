# pivot_root：仅看帮助，勿真切换根

TEST = {
    "order": 189,
    "name": "busybox_pivot_root",
    "cmd": "busybox pivot_root -h 2>&1",
    "expected_substring": "Usage",
    "expect_non_empty": True,
    "timeout": 2.0,
}
