# microcom：串口工具（无设备时多为用法/错误）

TEST = {
    "order": 148,
    "name": "busybox_microcom",
    "cmd": "busybox microcom -h 2>&1",
    "expected_substring": "Usage: microcom",
    "expect_non_empty": True,
    "timeout": 2.0,
}
