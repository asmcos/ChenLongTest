# find：根下查找 proc 目录名

TEST = {
    "order": 75,
    "name": "busybox_find",
    "cmd": "busybox find / -maxdepth 1 -name proc 2>&1",
    "expected_substring": "proc",
    "expect_non_empty": True,
    "timeout": 3.0,
}
