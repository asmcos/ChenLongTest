# insmod：无 ko 路径时多为用法/错误

TEST = {
    "order": 104,
    "name": "busybox_insmod",
    "cmd": "busybox insmod 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 2.0,
}
