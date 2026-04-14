# modprobe：仅看帮助，不随意 insmod

TEST = {
    "order": 158,
    "name": "busybox_modprobe",
    "cmd": "busybox modprobe -h 2>&1",
    "expected_substring": "Usage",
    "expect_non_empty": True,
    "timeout": 2.0,
}
