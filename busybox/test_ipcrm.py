# ipcrm：无参时多为用法/错误

TEST = {
    "order": 111,
    "name": "busybox_ipcrm",
    "cmd": "busybox ipcrm 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 2.0,
}
