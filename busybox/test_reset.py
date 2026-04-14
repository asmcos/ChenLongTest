# reset：终端复位（串口上可能无可见输出，跟一条 echo）

TEST = {
    "order": 210,
    "name": "busybox_reset",
    "cmd": "busybox reset 2>/dev/null; busybox echo reset_done 2>&1",
    "expected_substring": "reset_done",
    "expect_non_empty": True,
    "timeout": 2.0,
}
