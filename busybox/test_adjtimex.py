# busybox --list 中第 5 个 applet：adjtimex
# StarryOS 若未实现 adjtimex 系统调用，会打印 Function not implemented —— 应判 FAIL

TEST = {
    "order": 5,
    "name": "busybox_adjtimex",
    "cmd": "busybox adjtimex 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "fail_if_substrings": [
        "Function not implemented",
        "Unimplemented syscall",
    ],
    "timeout": 2.0,
}
