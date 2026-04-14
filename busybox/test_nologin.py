# nologin：拒绝登录提示

TEST = {
    "order": 174,
    "name": "busybox_nologin",
    "cmd": "busybox nologin 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 2.0,
}
