# halt：绝不真关机；仅请求帮助/用法类输出

TEST = {
    "order": 90,
    "name": "busybox_halt",
    "cmd": "busybox halt -h 2>&1",
    "expected_substring": "Usage",
    "expect_non_empty": True,
    "timeout": 2.0,
}
