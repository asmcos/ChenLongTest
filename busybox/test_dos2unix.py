# busybox_list.log：dnsdomainname 之后 — dos2unix（构造 CRLF 文件并转换）

TEST = {
    "order": 56,
    "name": "busybox_dos2unix",
    "cmd": "busybox sh -c 'busybox printf \"a\\r\\n\" > /tmp/bb_d2u && busybox dos2unix /tmp/bb_d2u && busybox od -An -tx1 /tmp/bb_d2u' 2>&1",
    "clean": "busybox sh -c 'busybox rm -f /tmp/bb_d2u' 2>&1",
    "expected_substring": "0a",
    "expect_non_empty": True,
    "timeout": 4.0,
}
