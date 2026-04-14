# fsync：创建文件后 fsync，再回读验证；用 clean 回收

TEST = {
    "order": 82,
    "name": "busybox_fsync",
    "cmd": "busybox sh -c 'busybox echo fsync_ok > /tmp/bb_fsync_t && busybox fsync /tmp/bb_fsync_t && busybox cat /tmp/bb_fsync_t' 2>&1",
    "clean": "busybox sh -c 'busybox rm -f /tmp/bb_fsync_t' 2>&1",
    "expected_substring": "fsync_ok",
    "expect_non_empty": True,
    "timeout": 4.0,
}
