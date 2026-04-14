# nproc：可用 CPU 数

TEST = {
    "order": 175,
    "name": "busybox_nproc",
    "cmd": "busybox sh -c 'n=$(busybox nproc) && busybox test -n \"$n\" && busybox echo nproc_ok' 2>&1",
    "expected_substring": "nproc_ok",
    "expect_non_empty": True,
    "timeout": 2.0,
}
