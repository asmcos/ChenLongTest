# ls：根目录列表，应含常见目录名（与 busybox_list 无关，独立一条）

TEST = {
    "order": 7,
    "name": "ls_root",
    "cmd": "ls /",
    "expected_substring": "bin",
    "expect_non_empty": True,
    "timeout": 2.0,
}
