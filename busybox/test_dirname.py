# busybox_list.log：diff 之后 — dirname

TEST = {
    "order": 53,
    "name": "busybox_dirname",
    "cmd": "busybox dirname /usr/bin/foo 2>&1",
    "expected_substring": "/usr/bin",
    "expect_non_empty": True,
    "timeout": 2.0,
}
