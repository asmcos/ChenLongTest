# kbd_mode：键盘模式（无 tty 时常为错误）

TEST = {
    "order": 118,
    "name": "busybox_kbd_mode",
    "cmd": "busybox kbd_mode -h 2>&1",
    "expected_substring": "Usage",
    "expect_non_empty": True,
    "timeout": 2.0,
}
