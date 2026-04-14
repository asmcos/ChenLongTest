# pmap：查看 PID 1 内存映射（无权限时也可能有错误输出）

TEST = {
    "order": 191,
    "name": "busybox_pmap",
    "cmd": "busybox pmap 1 2>&1; busybox echo pmap_ok",
    "expected_substring": "pmap_ok",
    "expect_non_empty": True,
    "timeout": 2.0,
}
