# sha256sum：管道校验

TEST = {
    "order": 231,
    "name": "busybox_sha256sum",
    "cmd": "busybox echo -n s256 | busybox sha256sum 2>&1",
    "expected_substring": "  -",
    "expect_non_empty": True,
    "timeout": 2.0,
}
