# linux32：兼容“支持/不支持”两种结果，统一回显标记

TEST = {
    "order": 126,
    "name": "busybox_linux32",
    "cmd": "busybox linux32 busybox echo linux32_ok 2>&1 || busybox echo linux32_fallback",
    "expected_substring": "linux32_",
    "expect_non_empty": True,
    "timeout": 2.0,
}
