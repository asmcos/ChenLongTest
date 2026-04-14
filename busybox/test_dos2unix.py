# busybox_list.log：dnsdomainname 之后 — dos2unix

TEST = {
    "order": 56,
    "name": "busybox_dos2unix",
    "cmd": "busybox dos2unix -h 2>&1",
    "expected_substring": "Usage",
    "expect_non_empty": True,
    "timeout": 2.0,
}
