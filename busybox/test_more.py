# more：分页读短文件（应很快结束）

TEST = {
    "order": 159,
    "name": "busybox_more",
    "cmd": "busybox more /proc/version 2>&1",
    "expected_substring": "Linux",
    "expect_non_empty": True,
    "timeout": 3.0,
}
