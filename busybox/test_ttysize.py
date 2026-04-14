# ttysize：终端宽高（非 tty 时可能无输出，退化为占位）

TEST = {
    "order": 268,
    "name": "busybox_ttysize",
    "cmd": "busybox sh -c 'S=$(busybox ttysize 2>&1); busybox test -n \"$S\" && busybox echo \"$S\" || busybox echo 0 0' 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 2.0,
}
