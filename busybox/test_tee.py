# tee：写文件且复制到 stdout

TEST = {
    "order": 255,
    "name": "busybox_tee",
    "cmd": "busybox sh -c 'busybox echo tee_line | busybox tee /tmp/bb_tee_f >/dev/null && busybox cat /tmp/bb_tee_f' 2>&1",
    "expected_substring": "tee_line",
    "expect_non_empty": True,
    "timeout": 2.0,
}
