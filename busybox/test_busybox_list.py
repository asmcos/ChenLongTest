# 与 logs/.../busybox_list.log 一致：列出 BusyBox applets

TEST = {
    "order": 6,
    "name": "busybox_list",
    "cmd": "busybox --list",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 3.0,
}
