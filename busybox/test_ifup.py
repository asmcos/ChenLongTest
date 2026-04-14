# ifup：无接口名时应有用法/错误（勿对真实接口 up）

TEST = {
    "order": 101,
    "name": "busybox_ifup",
    "cmd": "busybox ifup 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 2.0,
}
