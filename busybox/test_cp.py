# busybox_list.log：comm 之后 — cp（复制文件并校验内容）

TEST = {
    "order": 38,
    "name": "busybox_cp",
    "cmd": "busybox sh -c 'busybox echo cp_ok > /tmp/bb_cp_src && busybox cp /tmp/bb_cp_src /tmp/bb_cp_dst && busybox cat /tmp/bb_cp_dst' 2>&1",
    "clean": "busybox sh -c 'busybox rm -f /tmp/bb_cp_src /tmp/bb_cp_dst' 2>&1",
    "expected_substring": "cp_ok",
    "expect_non_empty": True,
    "timeout": 4.0,
}
