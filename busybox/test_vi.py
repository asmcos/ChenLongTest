# vi：编辑器，仅校验帮助（避免进入全屏交互）

TEST = {
    "order": 288,
    "name": "busybox_vi",
    "cmd": "busybox vi -h 2>&1",
    "expected_substring": "Usage: vi",
    "expect_non_empty": True,
    "timeout": 2.0,
}
