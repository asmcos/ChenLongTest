# mkpasswd：生成密码哈希（示例盐）

TEST = {
    "order": 154,
    "name": "busybox_mkpasswd",
    "cmd": "busybox mkpasswd -m md5 testpass 2>&1",
    "expected_substring": "$1$",
    "expect_non_empty": True,
    "timeout": 2.0,
}
