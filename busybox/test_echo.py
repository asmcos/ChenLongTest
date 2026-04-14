# busybox_list.log：dumpkmap 之后 — echo

TEST = {
    "order": 59,
    "name": "busybox_echo",
    "cmd": "busybox echo echo_ok 2>&1",
    "expected_substring": "echo_ok",
    "expect_non_empty": True,
    "timeout": 2.0,
}
