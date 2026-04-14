# busybox_list.log：du 之后 — dumpkmap

TEST = {
    "order": 58,
    "name": "busybox_dumpkmap",
    "cmd": "busybox dumpkmap -h 2>&1",
    "expected_substring": "Usage",
    "expect_non_empty": True,
    "timeout": 2.0,
}
