# tr：字符替换

TEST = {
    "order": 261,
    "name": "busybox_tr",
    "cmd": "busybox echo abc | busybox tr 'a-z' 'A-Z' 2>&1",
    "expected_substring": "ABC",
    "expect_non_empty": True,
    "timeout": 2.0,
}
