# loadkmap：无 map 文件时多为错误（勿读二进制到终端）

TEST = {
    "order": 130,
    "name": "busybox_loadkmap",
    "cmd": "busybox loadkmap 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 2.0,
}
