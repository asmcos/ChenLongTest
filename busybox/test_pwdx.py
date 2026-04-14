# pwdx：PID 1 的工作目录

TEST = {
    "order": 199,
    "name": "busybox_pwdx",
    "cmd": "busybox pwdx 1 2>&1; busybox echo pwdx_ok",
    "expected_substring": "pwdx_ok",
    "expect_non_empty": True,
    "timeout": 2.0,
}
