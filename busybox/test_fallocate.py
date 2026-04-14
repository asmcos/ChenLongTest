# fallocate：在 /tmp 创建零长度预分配（只读根分区时可失败，失败则应有错误输出）

TEST = {
    "order": 67,
    "name": "busybox_fallocate",
    "cmd": "busybox rm -f /tmp/bb_falloc_t && busybox touch /tmp/bb_falloc_t && busybox fallocate -l 0 /tmp/bb_falloc_t 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 2.0,
}
