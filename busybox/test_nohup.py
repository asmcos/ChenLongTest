# nohup：忽略挂起执行 echo

TEST = {
    "order": 173,
    "name": "busybox_nohup",
    "cmd": "busybox sh -c 'cd /tmp && busybox rm -f nohup.out && busybox nohup busybox echo nohup_ok' 2>&1",
    "expected_substring": "nohup_ok",
    "expect_non_empty": True,
    "timeout": 2.0,
}
