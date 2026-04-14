# false：退出码应为 1

TEST = {
    "order": 68,
    "name": "busybox_false",
    "cmd": "busybox false; busybox echo exit:$? 2>&1",
    "expected_substring": "exit:1",
    "expect_non_empty": True,
    "timeout": 2.0,
}
