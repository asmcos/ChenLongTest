# tail：读文件末尾

TEST = {
    "order": 253,
    "name": "busybox_tail",
    "cmd": "busybox tail -n 1 /proc/version 2>&1",
    "expected_substring": "Linux",
    "expect_non_empty": True,
    "timeout": 2.0,
}
