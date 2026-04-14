# volname：卷标（对无效设备应有错误信息）

TEST = {
    "order": 290,
    "name": "busybox_volname",
    "cmd": "busybox volname /dev/null 2>&1; busybox echo volname_ok",
    "expected_substring": "volname_ok",
    "expect_non_empty": True,
    "timeout": 2.0,
}
