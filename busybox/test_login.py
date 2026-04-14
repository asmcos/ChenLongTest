# login：仅看帮助，避免交互式登录

TEST = {
    "order": 132,
    "name": "busybox_login",
    "cmd": "busybox login -h 2>&1",
    "expected_substring": "Usage: login",
    "expect_non_empty": True,
    "timeout": 2.0,
}
