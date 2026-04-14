# fuser：查看谁在用路径（无进程时也可能只有提示）

TEST = {
    "order": 83,
    "name": "busybox_fuser",
    "cmd": "busybox fuser /tmp 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 2.0,
}
