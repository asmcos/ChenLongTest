# killall：列出信号（不杀进程）

TEST = {
    "order": 120,
    "name": "busybox_killall",
    "cmd": "busybox killall -l 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 2.0,
}
