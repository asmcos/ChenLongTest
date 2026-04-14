# wget：下载，仅校验帮助（避免外网）

TEST = {
    "order": 294,
    "name": "busybox_wget",
    "cmd": "busybox wget -h 2>&1",
    "expected_substring": "Usage: wget",
    "expect_non_empty": True,
    "timeout": 2.0,
}
