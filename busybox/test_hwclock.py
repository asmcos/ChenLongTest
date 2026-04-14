# hwclock：读硬件时钟（无权限时常为错误信息）

TEST = {
    "order": 96,
    "name": "busybox_hwclock",
    "cmd": "busybox hwclock -r 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 2.0,
}
