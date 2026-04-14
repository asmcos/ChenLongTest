# vconfig：8021q VLAN，仅校验帮助

TEST = {
    "order": 287,
    "name": "busybox_vconfig",
    "cmd": "busybox vconfig -h 2>&1",
    "expected_substring": "Usage: vconfig",
    "expect_non_empty": True,
    "timeout": 2.0,
}
