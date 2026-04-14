# zcat：gzip 流解压到 stdout

TEST = {
    "order": 303,
    "name": "busybox_zcat",
    "cmd": "busybox echo -n hello | busybox gzip -c | busybox zcat 2>&1",
    "expected_substring": "hello",
    "expect_non_empty": True,
    "timeout": 3.0,
}
