# lzma：压缩并解压回读，校验内容

TEST = {
    "order": 141,
    "name": "busybox_lzma",
    "cmd": "busybox rm -f /tmp/bb_lzma.txt /tmp/bb_lzma.txt.lzma && busybox echo -n lzma_t > /tmp/bb_lzma.txt && busybox lzma -kf /tmp/bb_lzma.txt && busybox lzma -dc /tmp/bb_lzma.txt.lzma 2>&1",
    "expected_substring": "lzma_t",
    "expect_non_empty": True,
    "clean": "busybox rm -f /tmp/bb_lzma.txt /tmp/bb_lzma.txt.lzma",
    "timeout": 2.0,
}
