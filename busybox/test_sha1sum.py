# sha1sum：管道校验

TEST = {
    "order": 230,
    "name": "busybox_sha1sum",
    "cmd": "busybox echo -n sha1_t | busybox sha1sum 2>&1",
    "expected_substring": "  -",
    "expect_non_empty": True,
    "timeout": 2.0,
}
