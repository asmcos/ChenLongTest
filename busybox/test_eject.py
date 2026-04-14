# egrep 之后第 1 个：eject（无光驱时常为错误信息，仅断言有输出）

TEST = {
    "order": 61,
    "name": "busybox_eject",
    "cmd": "busybox eject 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 2.0,
}
