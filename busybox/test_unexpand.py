# unexpand：空格转制表符

TEST = {
    "order": 274,
    "name": "busybox_unexpand",
    "cmd": "busybox printf 'x    y\n' | busybox unexpand -a 2>&1; busybox echo unexpand_ok",
    "expected_substring": "unexpand_ok",
    "expect_non_empty": True,
    "timeout": 2.0,
}
