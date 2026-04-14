# busybox_list.log：beep 之后 — blkdiscard（无设备参数时一般打印用法/错误）

TEST = {
    "order": 18,
    "name": "busybox_blkdiscard",
    "cmd": "busybox blkdiscard 2>&1",
    "expected_substring": "Usage: blkdiscard",
    "expect_non_empty": True,
    "timeout": 2.0,
}
