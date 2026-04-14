# mkdir：创建目录并列出

TEST = {
    "order": 149,
    "name": "busybox_mkdir",
    "cmd": "busybox rm -rf /tmp/bb_mkd_one && busybox mkdir -p /tmp/bb_mkd_one && busybox ls -d /tmp/bb_mkd_one 2>&1",
    "expected_substring": "bb_mkd_one",
    "expect_non_empty": True,
    "timeout": 2.0,
}
