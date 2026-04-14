# ipcs：System V IPC 摘要

TEST = {
    "order": 112,
    "name": "busybox_ipcs",
    "cmd": "busybox ipcs 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 2.0,
}
