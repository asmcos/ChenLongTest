# rmdir：删除空目录

TEST = {
    "order": 215,
    "name": "busybox_rmdir",
    "cmd": "busybox mkdir -p /tmp/bb_rmd && busybox rmdir /tmp/bb_rmd && busybox echo rmdir_ok 2>&1",
    "expected_substring": "rmdir_ok",
    "expect_non_empty": True,
    "timeout": 2.0,
}
