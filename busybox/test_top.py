# top：批处理模式跑一帧（避免交互）

TEST = {
    "order": 259,
    "name": "busybox_top",
    "cmd": "busybox top -b -n 1 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 8.0,
}
