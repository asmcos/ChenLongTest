# iprule：策略路由规则

TEST = {
    "order": 116,
    "name": "busybox_iprule",
    "cmd": "busybox ip rule show 2>&1; busybox echo iprule_ok",
    "expected_substring": "iprule_ok",
    "expect_non_empty": True,
    "timeout": 2.0,
}
