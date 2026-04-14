# busybox_list.log：crond 之后 — crontab（写入并读取定时任务）

TEST = {
    "order": 41,
    "name": "busybox_crontab",
    "cmd": "busybox sh -c 'busybox mkdir -p /tmp/bb_crontab_tabs && busybox printf \"* * * * * busybox echo cron_tab_ok >> /tmp/bb_crontab_hit\\n\" > /tmp/bb_crontab_job && busybox crontab -c /tmp/bb_crontab_tabs /tmp/bb_crontab_job && busybox crontab -c /tmp/bb_crontab_tabs -l' 2>&1",
    "clean": "busybox sh -c 'busybox crontab -c /tmp/bb_crontab_tabs -r 2>/dev/null || true; busybox rm -rf /tmp/bb_crontab_tabs /tmp/bb_crontab_job /tmp/bb_crontab_hit' 2>&1",
    "expected_substring": "cron_tab_ok",
    "expect_non_empty": True,
    "timeout": 4.0,
}
