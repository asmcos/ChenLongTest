# last：登录历史（无 wtmp 时可能为空，失败则改为 -h）

TEST = {
    "order": 123,
    "name": "busybox_last",
    "cmd": "busybox last 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 2.0,
}
