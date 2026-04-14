# sed：替换

TEST = {
    "order": 219,
    "name": "busybox_sed",
    "cmd": "busybox echo hello | busybox sed 's/hello/sed_ok/' 2>&1",
    "expected_substring": "sed_ok",
    "expect_non_empty": True,
    "timeout": 2.0,
}
