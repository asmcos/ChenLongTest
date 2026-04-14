# busybox_list.log：dc 之后 — dd（创建文件并拷贝校验）

TEST = {
    "order": 46,
    "name": "busybox_dd",
    "cmd": "busybox sh -c 'busybox echo dd_ok > /tmp/bb_dd_in && busybox dd if=/tmp/bb_dd_in of=/tmp/bb_dd_out bs=1 count=6 2>/tmp/bb_dd_stat && busybox cat /tmp/bb_dd_out' 2>&1",
    "clean": "busybox sh -c 'busybox rm -f /tmp/bb_dd_in /tmp/bb_dd_out /tmp/bb_dd_stat' 2>&1",
    "expected_substring": "dd_ok",
    "expect_non_empty": True,
    "timeout": 4.0,
}
