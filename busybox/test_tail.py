# tail：读文件末尾

TEST = {
    "order": 253,
    "name": "busybox_tail",
    "cmd": "busybox tail -n 1 /etc/passwd 2>&1",
    "expected_substring": "root:",
    "expect_non_empty": True,
    "timeout": 2.0,
}
