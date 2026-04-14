# sort：排序行

TEST = {
    "order": 239,
    "name": "busybox_sort",
    "cmd": "busybox printf 'c\na\nb\n' | busybox sort 2>&1",
    "expected_substring": "a",
    "expect_non_empty": True,
    "timeout": 2.0,
}
