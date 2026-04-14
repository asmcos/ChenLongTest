# rdate：无 NTP 服务器时多为错误

TEST = {
    "order": 201,
    "name": "busybox_rdate",
    "cmd": "busybox rdate -h 2>&1",
    "expected_substring": "Usage: rdate",
    "expect_non_empty": True,
    "timeout": 3.0,
}
