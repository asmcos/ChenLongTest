# mesg：tty 消息开关（无 tty 时常为错误）

TEST = {
    "order": 147,
    "name": "busybox_mesg",
    "cmd": "busybox mesg 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 2.0,
}
