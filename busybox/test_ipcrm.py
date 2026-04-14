# ipcrm：帮助输出更稳定

TEST = {
    "order": 111,
    "name": "busybox_ipcrm",
    "cmd": "busybox ipcrm -h 2>&1",
    "expected_substring": "Usage: ipcrm",
    "expect_non_empty": True,
    "timeout": 2.0,
}
