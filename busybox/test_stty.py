# stty：终端属性（串口上应有输出）

TEST = {
    "order": 243,
    "name": "busybox_stty",
    "cmd": "busybox stty -a 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 2.0,
}
