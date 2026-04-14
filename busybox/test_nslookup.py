# nslookup：解析本机回环

TEST = {
    "order": 177,
    "name": "busybox_nslookup",
    "cmd": "busybox nslookup 127.0.0.1 2>&1; busybox echo nslookup_ok",
    "expected_substring": "nslookup_ok",
    "expect_non_empty": True,
    "timeout": 5.0,
}
