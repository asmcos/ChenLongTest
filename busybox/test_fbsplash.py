# fbsplash：帮助输出（避免依赖帧缓冲设备）

TEST = {
    "order": 71,
    "name": "busybox_fbsplash",
    "cmd": "busybox fbsplash -h 2>&1",
    "expected_substring": "Usage: fbsplash",
    "expect_non_empty": True,
    "timeout": 2.0,
}
