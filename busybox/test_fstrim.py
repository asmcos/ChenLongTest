# fstrim：仅测帮助输出，避免对挂载点做真实 trim

TEST = {
    "order": 81,
    "name": "busybox_fstrim",
    "cmd": "busybox fstrim -h 2>&1",
    "expected_substring": "Usage: fstrim",
    "expect_non_empty": True,
    "timeout": 2.0,
}
