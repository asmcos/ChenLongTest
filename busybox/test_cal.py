# busybox_list.log：bzip2 之后 — cal（打印日历）

TEST = {
    "order": 25,
    "name": "busybox_cal",
    "cmd": "busybox cal 2>&1",
    "expected_substring": "Su Mo Tu We Th Fr Sa",
    "expect_non_empty": True,
    "timeout": 2.0,
}
