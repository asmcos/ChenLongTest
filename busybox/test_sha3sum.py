# sha3sum：管道校验

TEST = {
    "order": 232,
    "name": "busybox_sha3sum",
    "cmd": "busybox echo -n s3 | busybox sha3sum 2>&1",
    "expected_substring": "  -",
    "expect_non_empty": True,
    "timeout": 2.0,
}
