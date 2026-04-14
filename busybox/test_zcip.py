# zcip：BusyBox 小众工具，仅校验帮助

TEST = {
    "order": 304,
    "name": "busybox_zcip",
    "cmd": "busybox zcip -h 2>&1",
    "expected_substring": "Usage",
    "expect_non_empty": True,
    "timeout": 2.0,
}
