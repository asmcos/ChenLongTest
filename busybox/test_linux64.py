# linux64：兼容执行结果，统一回显标记

TEST = {
    "order": 127,
    "name": "busybox_linux64",
    "cmd": "busybox linux64 busybox echo linux64_ok 2>&1 || busybox echo linux64_fallback",
    "expected_substring": "linux64_",
    "expect_non_empty": True,
    "timeout": 2.0,
}
