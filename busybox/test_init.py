# init：仅看帮助，绝不执行切换运行级（勿无参当 PID1）

TEST = {
    "order": 102,
    "name": "busybox_init",
    "cmd": "busybox init -h 2>&1",
    "expected_substring": "Usage",
    "expect_non_empty": True,
    "timeout": 2.0,
}
