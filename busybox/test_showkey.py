# showkey：交互式，仅校验帮助

TEST = {
    "order": 234,
    "name": "busybox_showkey",
    "cmd": "busybox showkey -h 2>&1",
    "expected_substring": "Usage",
    "expect_non_empty": True,
    "timeout": 2.0,
}
