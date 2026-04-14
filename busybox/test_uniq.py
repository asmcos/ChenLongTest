# uniq：相邻重复行去重

TEST = {
    "order": 275,
    "name": "busybox_uniq",
    "cmd": "busybox printf 'a\na\nb\n' | busybox uniq 2>&1",
    "expected_substring": "b",
    "expect_non_empty": True,
    "timeout": 2.0,
}
