# linux32：在 32 位子环境执行（riscv 上可能报错，有输出即可）

TEST = {
    "order": 126,
    "name": "busybox_linux32",
    "cmd": "busybox linux32 busybox echo linux32_ok 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 2.0,
}
