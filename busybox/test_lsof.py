# lsof：打开文件列表（无权限时也可能有提示）

TEST = {
    "order": 138,
    "name": "busybox_lsof",
    "cmd": "busybox lsof 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 3.0,
}
