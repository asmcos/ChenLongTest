# nc：部分环境 -z 无 stdout；用帮助稳定断言

TEST = {
    "order": 168,
    "name": "busybox_nc",
    "cmd": "busybox nc -h 2>&1",
    "expected_substring": "Usage: nc",
    "expect_non_empty": True,
    "timeout": 2.0,
}
