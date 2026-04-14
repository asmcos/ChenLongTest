# more：分页读短文件（应很快结束）

TEST = {
    "order": 159,
    "name": "busybox_more",
    "cmd": "busybox more /etc/passwd 2>&1",
    "expected_substring": "root:",
    "expect_non_empty": True,
    "timeout": 3.0,
}
