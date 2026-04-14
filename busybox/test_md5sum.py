# md5sum：管道校验

TEST = {
    "order": 145,
    "name": "busybox_md5sum",
    "cmd": "busybox echo -n md5_t | busybox md5sum 2>&1",
    "expected_substring": "-",
    "expect_non_empty": True,
    "timeout": 2.0,
}
