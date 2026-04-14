# id：用户 id 信息

TEST = {
    "order": 97,
    "name": "busybox_id",
    "cmd": "busybox id 2>&1",
    "expected_substring": "uid=",
    "expect_non_empty": True,
    "timeout": 2.0,
}
