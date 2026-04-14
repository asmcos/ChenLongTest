# busybox_list.log：bunzip2 之后 — bzcat（压缩后通过 bzcat 读取）

TEST = {
    "order": 23,
    "name": "busybox_bzcat",
    "cmd": "busybox sh -c 'busybox echo bzcat_ok > /tmp/bb_bzcat_t && busybox bzip2 -f /tmp/bb_bzcat_t && busybox bzcat /tmp/bb_bzcat_t.bz2' 2>&1",
    "clean": "busybox sh -c 'busybox rm -f /tmp/bb_bzcat_t /tmp/bb_bzcat_t.bz2' 2>&1",
    "expected_substring": "bzcat_ok",
    "expect_non_empty": True,
    "timeout": 4.0,
}
