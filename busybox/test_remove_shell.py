# remove-shell：无参时多为用法（勿真改登录 shell）

TEST = {
    "order": 208,
    "name": "busybox_remove_shell",
    "cmd": "busybox remove-shell -h 2>&1",
    "expected_substring": "Usage: remove-shell",
    "expect_non_empty": True,
    "timeout": 2.0,
}
