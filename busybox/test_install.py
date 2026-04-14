# install：复制文件并设权限

TEST = {
    "order": 105,
    "name": "busybox_install",
    "cmd": "busybox rm -f /tmp/bb_inst_dst /tmp/bb_inst_src && busybox echo ok > /tmp/bb_inst_src && busybox install -m 644 /tmp/bb_inst_src /tmp/bb_inst_dst && busybox cat /tmp/bb_inst_dst 2>&1",
    "expected_substring": "ok",
    "expect_non_empty": True,
    "timeout": 2.0,
}
