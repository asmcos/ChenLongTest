# partprobe：无块设备时多为错误

TEST = {
    "order": 181,
    "name": "busybox_partprobe",
    "cmd": "busybox partprobe 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 2.0,
}
