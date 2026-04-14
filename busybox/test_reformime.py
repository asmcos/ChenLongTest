# reformime：无输入时多为用法

TEST = {
    "order": 207,
    "name": "busybox_reformime",
    "cmd": "busybox reformime -h 2>&1",
    "expected_substring": "Usage: reformime",
    "expect_non_empty": True,
    "timeout": 2.0,
}
