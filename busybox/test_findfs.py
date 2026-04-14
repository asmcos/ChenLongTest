# findfs：无参时通常打印用法/错误

TEST = {
    "order": 76,
    "name": "busybox_findfs",
    "cmd": "busybox findfs 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 2.0,
}
