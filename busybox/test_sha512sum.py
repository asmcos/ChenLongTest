# sha512sum：管道校验

TEST = {
    "order": 233,
    "name": "busybox_sha512sum",
    "cmd": "busybox echo -n s512 | busybox sha512sum 2>&1",
    "expected_substring": "  -",
    "expect_non_empty": True,
    "timeout": 2.0,
}
