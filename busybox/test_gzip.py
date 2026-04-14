# gzip：压缩文件并校验产物非空

TEST = {
    "order": 89,
    "name": "busybox_gzip",
    "cmd": "busybox sh -c 'busybox echo -n hello > /tmp/bb_gzip_t && busybox gzip -f /tmp/bb_gzip_t && busybox test -s /tmp/bb_gzip_t.gz && busybox echo gzip_ok' 2>&1",
    "clean": "busybox sh -c 'busybox rm -f /tmp/bb_gzip_t /tmp/bb_gzip_t.gz' 2>&1",
    "expected_substring": "gzip_ok",
    "expect_non_empty": True,
    "timeout": 4.0,
}
