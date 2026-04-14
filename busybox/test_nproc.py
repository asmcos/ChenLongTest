# nproc：可用 CPU 数

TEST = {
    "order": 175,
    "name": "busybox_nproc",
    "cmd": "busybox nproc 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 2.0,
}
