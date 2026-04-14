# busybox_list.log：dirname 之后 — dmesg（直接读可能需权限；用帮助稳定断言）

TEST = {
    "order": 54,
    "name": "busybox_dmesg",
    "cmd": "busybox dmesg -h 2>&1",
    "expected_substring": "Usage: dmesg",
    "expect_non_empty": True,
    "timeout": 2.0,
}
