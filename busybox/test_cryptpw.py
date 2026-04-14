# busybox_list.log：crontab 之后 — cryptpw

TEST = {
    "order": 42,
    "name": "busybox_cryptpw",
    "cmd": "busybox cryptpw -h 2>&1",
    "expected_substring": "Usage",
    "expect_non_empty": True,
    "timeout": 2.0,
}
