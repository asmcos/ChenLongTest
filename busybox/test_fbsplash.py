# fbsplash：无参数时多为错误/提示，要求有输出

TEST = {
    "order": 71,
    "name": "busybox_fbsplash",
    "cmd": "busybox fbsplash 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 2.0,
}
