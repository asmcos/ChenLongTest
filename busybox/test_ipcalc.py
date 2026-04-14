# ipcalc：网段计算

TEST = {
    "order": 110,
    "name": "busybox_ipcalc",
    "cmd": "busybox ipcalc 192.168.1.1/24 2>&1",
    "expected_substring": "NETMASK=",
    "expect_non_empty": True,
    "timeout": 2.0,
}
