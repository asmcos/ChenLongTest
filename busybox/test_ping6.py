# ping6：无 IPv6 时常失败；有输出即可

TEST = {
    "order": 187,
    "name": "busybox_ping6",
    "cmd": "busybox ping6 -c 1 ::1 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 5.0,
}
