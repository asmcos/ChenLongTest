# tree：目录树

TEST = {
    "order": 264,
    "name": "busybox_tree",
    "cmd": "busybox sh -c 'busybox mkdir -p /tmp/bb_tree/d && busybox echo x > /tmp/bb_tree/d/a && busybox tree /tmp/bb_tree 2>&1'",
    "expected_substring": "a",
    "expect_non_empty": True,
    "timeout": 3.0,
}
