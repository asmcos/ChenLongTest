# busybox_list.log：arp 之后 — arping

TEST = {
    "order": 10,
    "name": "busybox_arping",
    "cmd": "busybox arping 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 2.0,
}
