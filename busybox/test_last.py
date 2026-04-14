# last：在该环境中直接校验帮助，避免 wtmp 为空导致不稳定

TEST = {
    "order": 123,
    "name": "busybox_last",
    "cmd": "busybox last -h 2>&1",
    "expected_substring": "Usage: last",
    "expect_non_empty": True,
    "timeout": 2.0,
}
