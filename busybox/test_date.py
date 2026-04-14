# busybox_list.log：cut 之后 — date

TEST = {
    "order": 44,
    "name": "busybox_date",
    "cmd": "busybox date 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 2.0,
}
