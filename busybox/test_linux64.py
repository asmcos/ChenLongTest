# linux64：在 64 位子环境执行 echo

TEST = {
    "order": 127,
    "name": "busybox_linux64",
    "cmd": "busybox linux64 busybox echo linux64_ok 2>&1",
    "expected_substring": "linux64_ok",
    "expect_non_empty": True,
    "timeout": 2.0,
}
