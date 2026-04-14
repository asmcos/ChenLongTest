# fuser：帮助输出稳定，不依赖具体文件占用者

TEST = {
    "order": 83,
    "name": "busybox_fuser",
    "cmd": "busybox fuser -h 2>&1",
    "expected_substring": "Usage: fuser",
    "expect_non_empty": True,
    "timeout": 2.0,
}
