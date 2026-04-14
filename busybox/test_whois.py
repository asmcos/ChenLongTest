# whois：查询注册信息，仅校验帮助（避免外网）

TEST = {
    "order": 298,
    "name": "busybox_whois",
    "cmd": "busybox whois -h 2>&1",
    "expected_substring": "Usage: whois",
    "expect_non_empty": True,
    "timeout": 2.0,
}
