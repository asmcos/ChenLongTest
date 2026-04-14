# sync：刷盘（静默）后 echo

TEST = {
    "order": 249,
    "name": "busybox_sync",
    "cmd": "busybox sync && busybox echo sync_ok 2>&1",
    "expected_substring": "sync_ok",
    "expect_non_empty": True,
    "timeout": 3.0,
}
