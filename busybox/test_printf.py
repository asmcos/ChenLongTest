# printf：格式化输出

TEST = {
    "order": 194,
    "name": "busybox_printf",
    "cmd": "busybox printf 'pf_%s_ok\\n' bb 2>&1",
    "expected_substring": "pf_bb_ok",
    "expect_non_empty": True,
    "timeout": 2.0,
}
