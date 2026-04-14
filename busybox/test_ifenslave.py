# ifenslave：无参时多为用法/错误

TEST = {
    "order": 100,
    "name": "busybox_ifenslave",
    "cmd": "busybox ifenslave 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 2.0,
}
