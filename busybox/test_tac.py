# tac：逆序行

TEST = {
    "order": 252,
    "name": "busybox_tac",
    "cmd": "busybox printf 'a\nb\n' | busybox tac 2>&1",
    "expected_substring": "b",
    "expect_non_empty": True,
    "timeout": 2.0,
}
