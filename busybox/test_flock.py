# flock：对 /tmp 文件加独占锁并执行子命令

TEST = {
    "order": 77,
    "name": "busybox_flock",
    "cmd": "busybox rm -f /tmp/bb_flock_t && busybox touch /tmp/bb_flock_t && busybox flock -x /tmp/bb_flock_t -c 'busybox echo flock_ok' 2>&1",
    "expected_substring": "flock_ok",
    "expect_non_empty": True,
    "timeout": 2.0,
}
