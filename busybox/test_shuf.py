# shuf：打乱行

TEST = {
    "order": 236,
    "name": "busybox_shuf",
    "cmd": "busybox printf 'a\nb\nc\n' | busybox shuf 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 2.0,
}
