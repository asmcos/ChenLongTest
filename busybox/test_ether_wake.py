# ether-wake：无参时通常打印用法或错误，避免纯 -h

TEST = {
    "order": 63,
    "name": "busybox_ether_wake",
    "cmd": "busybox ether-wake 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 2.0,
}
