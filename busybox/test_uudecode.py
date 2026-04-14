# uudecode：解 uu 编码（与 uuencode 管道自洽）

TEST = {
    "order": 285,
    "name": "busybox_uudecode",
    "cmd": "busybox sh -c 'busybox echo hi | busybox uuencode out | busybox uudecode -o /tmp/bb_uudec 2>&1 && busybox cat /tmp/bb_uudec' 2>&1",
    "expected_substring": "hi",
    "expect_non_empty": True,
    "clean": "busybox rm -f /tmp/bb_uudec",
    "timeout": 3.0,
}
