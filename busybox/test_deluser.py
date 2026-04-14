# busybox_list.log：delgroup 之后 — deluser（与 adduser 定制测试不同；此处仅测帮助）

TEST = {
    "order": 49,
    "name": "busybox_deluser",
    "cmd": "busybox deluser -h 2>&1",
    "expected_substring": "Usage",
    "expect_non_empty": True,
    "timeout": 2.0,
}
