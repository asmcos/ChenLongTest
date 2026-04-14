# busybox_list.log：bzcat 之后 — bzip2（创建文件并压缩，校验 .bz2 产物）

TEST = {
    "order": 24,
    "name": "busybox_bzip2",
    "cmd": "busybox sh -c 'busybox echo bz2_ok > /tmp/bb_bzip2_t && busybox bzip2 -kf /tmp/bb_bzip2_t && busybox test -f /tmp/bb_bzip2_t.bz2 && busybox echo bzip2_ok' 2>&1",
    "clean": "busybox sh -c 'busybox rm -f /tmp/bb_bzip2_t /tmp/bb_bzip2_t.bz2' 2>&1",
    "expected_substring": "bzip2_ok",
    "expect_non_empty": True,
    "timeout": 4.0,
}
