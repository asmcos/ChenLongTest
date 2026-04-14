# nice：降低优先级执行 echo

TEST = {
    "order": 170,
    "name": "busybox_nice",
    "cmd": "busybox nice -n 10 busybox echo nice_ok 2>&1",
    "expected_substring": "nice_ok",
    "expect_non_empty": True,
    "timeout": 2.0,
}
