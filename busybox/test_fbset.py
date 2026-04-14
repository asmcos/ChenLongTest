# fbset：无帧缓冲时 -i 可能失败；有输出即可（错误也算）

TEST = {
    "order": 70,
    "name": "busybox_fbset",
    "cmd": "busybox fbset -i 2>&1",
    "expected_substring": "option 'i' not handled",
    "expect_non_empty": True,
    "timeout": 2.0,
}
