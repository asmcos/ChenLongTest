# ifdown：无接口名时应有用法/错误（勿对真实接口 down）

TEST = {
    "order": 99,
    "name": "busybox_ifdown",
    "cmd": "busybox ifdown 2>&1",
    "expected_substring": "ifdown",
    "expect_non_empty": True,
    "timeout": 2.0,
}
