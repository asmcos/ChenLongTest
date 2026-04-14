# gunzip：与 gzip 管道往返还原字符串

TEST = {
    "order": 88,
    "name": "busybox_gunzip",
    "cmd": "busybox echo -n hello | busybox gzip -c | busybox gunzip -c 2>&1",
    "expected_substring": "hello",
    "expect_non_empty": True,
    "timeout": 2.0,
}
