# busybox_list.log：bc 之后 — beep（当前镜像常返回控制台不可用）

TEST = {
    "order": 17,
    "name": "busybox_beep",
    "cmd": "busybox beep 2>&1",
    "expected_substring": "can't open console",
    "expect_non_empty": True,
    "timeout": 2.0,
}
