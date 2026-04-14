# setsid：新会话中执行 echo

TEST = {
    "order": 228,
    "name": "busybox_setsid",
    "cmd": "busybox setsid busybox echo setsid_ok 2>&1",
    "expected_substring": "setsid_ok",
    "expect_non_empty": True,
    "timeout": 2.0,
}
