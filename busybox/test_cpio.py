# busybox_list.log：cp 之后 — cpio（生成 newc 包并校验产物非空）

TEST = {
    "order": 39,
    "name": "busybox_cpio",
    "cmd": "busybox sh -c 'busybox mkdir -p /tmp/bb_cpio && busybox echo cpio_ok > /tmp/bb_cpio/in && (cd /tmp/bb_cpio && busybox echo in | busybox cpio -o -H newc > out.cpio) && busybox test -s /tmp/bb_cpio/out.cpio && busybox echo cpio_ok' 2>&1",
    "clean": "busybox sh -c 'busybox rm -rf /tmp/bb_cpio' 2>&1",
    "expected_substring": "cpio_ok",
    "expect_non_empty": True,
    "timeout": 5.0,
}
