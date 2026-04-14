# busybox_list.log：clear 之后 — cmp（构造两份相同文件进行比较）

TEST = {
    "order": 36,
    "name": "busybox_cmp",
    "cmd": "busybox sh -c 'busybox echo cmp_ok > /tmp/bb_cmp_a && busybox cp /tmp/bb_cmp_a /tmp/bb_cmp_b && busybox cmp /tmp/bb_cmp_a /tmp/bb_cmp_b && busybox echo cmp_ok' 2>&1",
    "clean": "busybox sh -c 'busybox rm -f /tmp/bb_cmp_a /tmp/bb_cmp_b' 2>&1",
    "expected_substring": "cmp_ok",
    "expect_non_empty": True,
    "timeout": 4.0,
}
