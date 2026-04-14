# arch：返回体系结构；StarryOS 当前为 riscv64

TEST = {
    "order": 8,
    "name": "busybox_arch",
    "cmd": "busybox arch 2>&1",
    "expected_substring": "riscv",
    "expect_non_empty": True,
    "timeout": 2.0,
}
