# link：硬链接同一文件内容

TEST = {
    "order": 125,
    "name": "busybox_link",
    "cmd": "busybox rm -f /tmp/bb_link_a /tmp/bb_link_b && busybox echo hi > /tmp/bb_link_a && busybox link /tmp/bb_link_a /tmp/bb_link_b && busybox cat /tmp/bb_link_b 2>&1",
    "expected_substring": "hi",
    "expect_non_empty": True,
    "timeout": 2.0,
}
