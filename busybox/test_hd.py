# hd：对稳定文本文件做十六进制查看

TEST = {
    "order": 91,
    "name": "busybox_hd",
    "cmd": "busybox hd -n 64 /etc/passwd 2>&1",
    "expected_substring": "00000000",
    "expect_non_empty": True,
    "timeout": 2.0,
}
