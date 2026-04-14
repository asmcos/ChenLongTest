# fatattr：非 FAT 上常为错误信息，断言有输出

TEST = {
    "order": 69,
    "name": "busybox_fatattr",
    "cmd": "busybox fatattr -v / 2>&1",
    "expected_substring": "fatattr:",
    "expect_non_empty": True,
    "timeout": 2.0,
}
