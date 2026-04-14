# renice：在子 shell 中对自身 PID 调优先级（+0 无害）

TEST = {
    "order": 209,
    "name": "busybox_renice",
    "cmd": "busybox sh -c 'busybox renice +0 -p $$' 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 2.0,
}

