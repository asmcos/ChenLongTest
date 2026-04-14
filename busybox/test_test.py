# test：条件判断（applet 名 test）

TEST = {
    "order": 256,
    "name": "busybox_test",
    "cmd": "busybox test 1 -eq 1 && busybox echo test_ok 2>&1",
    "expected_substring": "test_ok",
    "expect_non_empty": True,
    "timeout": 2.0,
}
