# pkill：仅列信号/帮助，勿杀进程

TEST = {
    "order": 190,
    "name": "busybox_pkill",
    "cmd": "busybox pkill -l 2>&1",
    "expected_substring": "HUP",
    "expect_non_empty": True,
    "timeout": 2.0,
}
