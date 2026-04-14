# hostid：主机标识（部分环境可能无输出，失败再放宽）

TEST = {
    "order": 94,
    "name": "busybox_hostid",
    "cmd": "busybox hostid 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 2.0,
}
