# busybox_list.log：arch 之后 — arp

TEST = {
    "order": 9,
    "name": "busybox_arp",
    "cmd": "busybox arp 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 2.0,
}
