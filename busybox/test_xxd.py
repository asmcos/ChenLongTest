# xxd：十六进制转储

TEST = {
    "order": 300,
    "name": "busybox_xxd",
    "cmd": "busybox printf 'Hi' | busybox xxd 2>&1",
    "expected_substring": "48 69",
    "expect_non_empty": True,
    "timeout": 2.0,
}
