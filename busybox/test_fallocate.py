# fallocate：创建文件并分配 1KB，校验文件大小

TEST = {
    "order": 67,
    "name": "busybox_fallocate",
    "cmd": "busybox sh -c 'busybox rm -f /tmp/bb_falloc_t && busybox touch /tmp/bb_falloc_t && busybox fallocate -l 1024 /tmp/bb_falloc_t && busybox ls -ln /tmp/bb_falloc_t' 2>&1",
    "clean": "busybox sh -c 'busybox rm -f /tmp/bb_falloc_t' 2>&1",
    "expected_substring": " 1024 ",
    "expect_non_empty": True,
    "timeout": 4.0,
}
