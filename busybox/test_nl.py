# nl：带行号输出

TEST = {
    "order": 171,
    "name": "busybox_nl",
    "cmd": "busybox nl -ba /proc/version 2>&1",
    "expected_substring": "Linux",
    "expect_non_empty": True,
    "timeout": 2.0,
}
