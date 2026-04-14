# mkfifo：创建命名管道并 ls 可见

TEST = {
    "order": 151,
    "name": "busybox_mkfifo",
    "cmd": "busybox rm -f /tmp/bb_fifo_t && busybox mkfifo /tmp/bb_fifo_t && busybox ls -l /tmp/bb_fifo_t 2>&1",
    "expected_substring": "bb_fifo_t",
    "expect_non_empty": True,
    "clean": "busybox rm -f /tmp/bb_fifo_t",
    "timeout": 2.0,
}
