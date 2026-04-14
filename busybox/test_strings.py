# strings：从二进制提取可打印串

TEST = {
    "order": 242,
    "name": "busybox_strings",
    "cmd": "busybox strings /bin/busybox 2>&1",
    "expected_substring": "BusyBox",
    "expect_non_empty": True,
    "timeout": 3.0,
}
