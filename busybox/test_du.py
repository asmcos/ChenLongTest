# du：勿用 du -s /（根目录扫描极慢且长时间无输出，易触发 harness 超时并占满 shell）

TEST = {
    "order": 57,
    "name": "busybox_du",
    "cmd": "busybox sh -c 'busybox mkdir -p /tmp/bb_du && busybox du -s /tmp/bb_du' 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 5.0,
}
