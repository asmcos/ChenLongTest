# busybox_list.log：crond 之后 — crontab

TEST = {
    "order": 41,
    "name": "busybox_crontab",
    "cmd": "busybox crontab -h 2>&1",
    "expected_substring": "Usage",
    "expect_non_empty": True,
    "timeout": 2.0,
}
