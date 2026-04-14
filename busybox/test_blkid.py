# busybox_list.log：blkdiscard 之后 — blkid（无块设备时输出可能为空，用 -h 校验）

TEST = {
    "order": 19,
    "name": "busybox_blkid",
    "cmd": "busybox blkid -h 2>&1",
    "expected_substring": "Usage",
    "expect_non_empty": True,
    "timeout": 2.0,
}
