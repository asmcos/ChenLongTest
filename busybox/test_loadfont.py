# loadfont：无参会从 stdin 读字体数据，易长时间阻塞 shell；改为仅校验帮助

TEST = {
    "order": 129,
    "name": "busybox_loadfont",
    "cmd": "busybox loadfont -h 2>&1",
    "expected_substring": "Usage: loadfont",
    "expect_non_empty": True,
    "timeout": 3.0,
}
