# kill：列出信号名（不杀进程）

TEST = {
    "order": 119,
    "name": "busybox_kill",
    "cmd": "busybox kill -l 2>&1",
    "expected_substring": "HUP",
    "expect_non_empty": True,
    "timeout": 2.0,
}
