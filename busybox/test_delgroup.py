# busybox_list.log：deallocvt 之后 — delgroup（与 addgroup 测试不同；此处仅测帮助）

TEST = {
    "order": 48,
    "name": "busybox_delgroup",
    "cmd": "busybox delgroup -h 2>&1",
    "expected_substring": "Usage",
    "expect_non_empty": True,
    "timeout": 2.0,
}
