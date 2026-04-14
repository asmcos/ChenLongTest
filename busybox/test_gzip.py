# gzip：压缩 stdout 应有输出（魔数/二进制）

TEST = {
    "order": 89,
    "name": "busybox_gzip",
    "cmd": "busybox echo -n hello | busybox gzip -c 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 2.0,
}
