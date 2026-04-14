# iprule：策略路由规则

TEST = {
    "order": 116,
    "name": "busybox_iprule",
    "cmd": "busybox iprule 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 2.0,
}
