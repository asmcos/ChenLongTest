# rdate：无 NTP 服务器时多为错误

TEST = {
    "order": 201,
    "name": "busybox_rdate",
    "cmd": "busybox rdate 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 3.0,
}
