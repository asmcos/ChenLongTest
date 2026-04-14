# loadfont：无字体文件时多为错误

TEST = {
    "order": 129,
    "name": "busybox_loadfont",
    "cmd": "busybox loadfont 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 2.0,
}
