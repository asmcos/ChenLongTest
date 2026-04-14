# nanddump：仅看帮助，勿对真实 MTD 读

TEST = {
    "order": 165,
    "name": "busybox_nanddump",
    "cmd": "busybox nanddump -h 2>&1",
    "expected_substring": "Usage",
    "expect_non_empty": True,
    "timeout": 2.0,
}
