# insmod：帮助输出，避免真正加载模块

TEST = {
    "order": 104,
    "name": "busybox_insmod",
    "cmd": "busybox insmod -h 2>&1",
    "expected_substring": "Usage: insmod",
    "expect_non_empty": True,
    "timeout": 2.0,
}
