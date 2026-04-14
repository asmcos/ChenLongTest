# busybox_list.log：chgrp 之后 — chmod（创建文件并改为 600，ls -l 校验）

TEST = {
    "order": 29,
    "name": "busybox_chmod",
    "cmd": "busybox sh -c 'busybox echo m > /tmp/bb_chmod_t && busybox chmod 600 /tmp/bb_chmod_t && busybox ls -l /tmp/bb_chmod_t | busybox grep -q \"^-rw-------\" && busybox echo chmod_ok' 2>&1",
    "clean": "busybox sh -c 'busybox rm -f /tmp/bb_chmod_t' 2>&1",
    "expected_substring": "chmod_ok",
    "expect_non_empty": True,
    "timeout": 4.0,
}
