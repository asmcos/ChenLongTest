# killall5：向所有进程发信号（仅看帮助，勿真发）

TEST = {
    "order": 121,
    "name": "busybox_killall5",
    "cmd": "busybox killall5 -h 2>&1",
    "expected_substring": "Usage: killall5",
    "expect_non_empty": True,
    "timeout": 2.0,
}
