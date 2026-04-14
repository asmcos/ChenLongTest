# tar：打包并列目录

TEST = {
    "order": 254,
    "name": "busybox_tar",
    "cmd": "busybox sh -c 'busybox mkdir -p /tmp/bb_tar && busybox echo z > /tmp/bb_tar/one && busybox tar -cf /tmp/bb_tar/t.tar -C /tmp/bb_tar one && busybox tar -tf /tmp/bb_tar/t.tar' 2>&1",
    "expected_substring": "one",
    "expect_non_empty": True,
    "clean": "busybox rm -rf /tmp/bb_tar",
    "timeout": 4.0,
}
