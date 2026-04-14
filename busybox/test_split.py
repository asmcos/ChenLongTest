# split：按字节切分文件

TEST = {
    "order": 240,
    "name": "busybox_split",
    "cmd": "busybox sh -c 'busybox mkdir -p /tmp/bb_spl && busybox echo abcdef > /tmp/bb_spl/in && busybox split -b2 /tmp/bb_spl/in /tmp/bb_spl/o && busybox cat /tmp/bb_spl/oaa' 2>&1",
    "expected_substring": "ab",
    "expect_non_empty": True,
    "timeout": 3.0,
}
