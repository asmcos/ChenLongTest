# busybox_list.log：cpio 之后 — crond（启动守护进程并校验已运行）

TEST = {
    "order": 40,
    "name": "busybox_crond",
    "cmd": "busybox sh -c 'busybox mkdir -p /tmp/bb_crond_tabs && busybox printf \"* * * * * busybox echo cron_tick >> /tmp/bb_crond_hit\\n\" > /tmp/bb_crond_job && busybox crontab -c /tmp/bb_crond_tabs /tmp/bb_crond_job && busybox crond -c /tmp/bb_crond_tabs -L /tmp/bb_crond_log && P=$(busybox pidof crond 2>/dev/null); busybox test -n \"$P\" && busybox echo crond_ok' 2>&1",
    "clean": "busybox sh -c 'busybox killall crond 2>/dev/null || true; busybox rm -rf /tmp/bb_crond_tabs /tmp/bb_crond_job /tmp/bb_crond_log /tmp/bb_crond_hit' 2>&1",
    "expected_substring": "crond_ok",
    "expect_non_empty": True,
    "timeout": 5.0,
}
