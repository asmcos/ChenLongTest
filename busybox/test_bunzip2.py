# busybox_list.log：brctl 之后 — bunzip2（先压缩再解压，校验原文）

TEST = {
    "order": 22,
    "name": "busybox_bunzip2",
    "cmd": "busybox sh -c 'busybox echo bunzip_ok > /tmp/bb_bunzip_t && busybox bzip2 -f /tmp/bb_bunzip_t && busybox bunzip2 -f /tmp/bb_bunzip_t.bz2 && busybox cat /tmp/bb_bunzip_t' 2>&1",
    "clean": "busybox sh -c 'busybox rm -f /tmp/bb_bunzip_t /tmp/bb_bunzip_t.bz2' 2>&1",
    "expected_substring": "bunzip_ok",
    "expect_non_empty": True,
    "timeout": 4.0,
}
