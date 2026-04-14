# fsync：对 /tmp 文件同步后打印标记（fsync 本身常无输出）

TEST = {
    "order": 82,
    "name": "busybox_fsync",
    "cmd": "busybox touch /tmp/bb_fsync_t && busybox fsync /tmp/bb_fsync_t && busybox echo fsync_ok 2>&1",
    "expected_substring": "fsync_ok",
    "expect_non_empty": True,
    "timeout": 2.0,
}
