# loadkmap：无参会从 stdin 读键盘映射，易阻塞；改为仅校验帮助

TEST = {
    "order": 130,
    "name": "busybox_loadkmap",
    "cmd": "busybox loadkmap -h 2>&1",
    "expected_substring": "Usage",
    "expect_non_empty": True,
    "timeout": 3.0,
}
