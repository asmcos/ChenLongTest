# seq：序列 1..3

TEST = {
    "order": 221,
    "name": "busybox_seq",
    "cmd": "busybox seq 1 3 2>&1",
    "expected_substring": "2",
    "expect_non_empty": True,
    "timeout": 2.0,
}
