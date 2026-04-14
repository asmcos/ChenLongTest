# busybox_list.log：cksum 之后 — clear（清屏常无 stdout；用 -h 出帮助）

TEST = {
    "order": 35,
    "name": "busybox_clear",
    "cmd": "busybox clear 2>&1; busybox echo clear_ok 2>&1",
    "expected_substring": "clear_ok",
    "expect_non_empty": True,
    "timeout": 2.0,
}
