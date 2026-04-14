# logread：读内核/日志环（无日志时可能空，可放宽）

TEST = {
    "order": 133,
    "name": "busybox_logread",
    "cmd": "busybox logread 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 3.0,
}
