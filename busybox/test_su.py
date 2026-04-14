# su：切换用户，仅校验帮助（避免交互）

TEST = {
    "order": 244,
    "name": "busybox_su",
    "cmd": "busybox su -h 2>&1",
    "expected_substring": "Usage: su",
    "expect_non_empty": True,
    "timeout": 2.0,
}
