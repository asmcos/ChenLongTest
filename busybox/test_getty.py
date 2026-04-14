# getty：无 tty 时多为错误/用法，仅要求有输出（勿无参挂住串口）

TEST = {
    "order": 85,
    "name": "busybox_getty",
    "cmd": "busybox getty 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 2.0,
}
