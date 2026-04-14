# busybox_list.log：arping 之后 — ash（不可无参交互，使用 -c）

TEST = {
    "order": 11,
    "name": "busybox_ash",
    "cmd": "busybox ash -c 'echo ash_ok' 2>&1",
    "expected_substring": "ash_ok",
    "expect_non_empty": True,
    "timeout": 2.0,
}
