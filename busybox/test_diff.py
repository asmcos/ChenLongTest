# busybox_list.log：df 之后 — diff（构造差异文件并验证 diff 输出）

TEST = {
    "order": 52,
    "name": "busybox_diff",
    "cmd": "busybox sh -c 'busybox echo left > /tmp/bb_diff_l && busybox echo right > /tmp/bb_diff_r && busybox diff /tmp/bb_diff_l /tmp/bb_diff_r > /tmp/bb_diff_o 2>&1; busybox grep -q \"^--- /tmp/bb_diff_l\" /tmp/bb_diff_o && busybox echo diff_ok' 2>&1",
    "clean": "busybox sh -c 'busybox rm -f /tmp/bb_diff_l /tmp/bb_diff_r /tmp/bb_diff_o' 2>&1",
    "expected_substring": "diff_ok",
    "expect_non_empty": True,
    "timeout": 4.0,
}
