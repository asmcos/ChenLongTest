# run-parts：执行目录下脚本

TEST = {
    "order": 218,
    "name": "busybox_run_parts",
    "cmd": "busybox rm -rf /tmp/bb_rp && busybox mkdir -p /tmp/bb_rp/d && busybox echo 'busybox echo rp_ok' > /tmp/bb_rp/d/00t && busybox chmod +x /tmp/bb_rp/d/00t && busybox run-parts /tmp/bb_rp/d 2>&1",
    "expected_substring": "rp_ok",
    "expect_non_empty": True,
    "timeout": 2.0,
}
