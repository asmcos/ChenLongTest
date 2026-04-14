# lzop：压缩并解压回读，校验内容

TEST = {
    "order": 142,
    "name": "busybox_lzop",
    "cmd": "busybox rm -f /tmp/bb_lzop.txt /tmp/bb_lzop.txt.lzo && busybox echo -n lzop_t > /tmp/bb_lzop.txt && busybox lzop -f /tmp/bb_lzop.txt && busybox lzop -dc /tmp/bb_lzop.txt.lzo 2>&1",
    "expected_substring": "lzop_t",
    "expect_non_empty": True,
    "clean": "busybox rm -f /tmp/bb_lzop.txt /tmp/bb_lzop.txt.lzo",
    "timeout": 2.0,
}
