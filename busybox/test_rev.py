# rev：反转行

TEST = {
    "order": 212,
    "name": "busybox_rev",
    "cmd": "busybox echo abcd | busybox rev 2>&1",
    "expected_substring": "dcba",
    "expect_non_empty": True,
    "timeout": 2.0,
}
