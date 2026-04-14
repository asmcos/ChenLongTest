# wc：行数统计

TEST = {
    "order": 293,
    "name": "busybox_wc",
    "cmd": "busybox printf 'a\nb\nc\n' | busybox wc -l 2>&1",
    "expected_substring": "3",
    "expect_non_empty": True,
    "timeout": 2.0,
}
