# busybox_list.log：dmesg 之后 — dnsdomainname（无域时 stdout 可能为空，用 -h）

TEST = {
    "order": 55,
    "name": "busybox_dnsdomainname",
    "cmd": "busybox dnsdomainname -h 2>&1",
    "expected_substring": "Usage",
    "expect_non_empty": True,
    "timeout": 2.0,
}
