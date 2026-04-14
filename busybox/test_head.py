# head：读取稳定文件首行

TEST = {
    "order": 92,
    "name": "busybox_head",
    "cmd": "busybox head -n 1 /etc/passwd 2>&1",
    "expected_substring": "root:",
    "expect_non_empty": True,
    "timeout": 2.0,
}
