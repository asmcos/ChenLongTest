# busybox_list.log：date 之后 — dc（RPN：2 2 + p）

TEST = {
    "order": 45,
    "name": "busybox_dc",
    "cmd": "busybox echo '2 2 + p' | busybox dc 2>&1",
    "expected_substring": "4",
    "expect_non_empty": True,
    "timeout": 2.0,
}
