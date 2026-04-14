# getopt：解析短选项

TEST = {
    "order": 84,
    "name": "busybox_getopt",
    "cmd": "busybox getopt -o ab: -- -a -b bar 2>&1",
    "expected_substring": "-- -a -b 'bar'",
    "expect_non_empty": True,
    "timeout": 2.0,
}
