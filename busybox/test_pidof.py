# pidof：查找 init 的 pid

TEST = {
    "order": 185,
    "name": "busybox_pidof",
    "cmd": "busybox pidof -s init 2>&1 || busybox pidof -s sh 2>&1",
    "expected_substring": "1",
    "expect_non_empty": True,
    "timeout": 2.0,
}
