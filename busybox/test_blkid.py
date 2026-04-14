# busybox_list.log：blkdiscard 之后 — blkid（本镜像对 -h 常无输出，改测无效设备错误）

TEST = {
    "order": 19,
    "name": "busybox_blkid",
    "cmd": "busybox blkid /dev/null 2>&1",
    "expected_substring": "/dev/null",
    "expect_non_empty": True,
    "timeout": 2.0,
}
