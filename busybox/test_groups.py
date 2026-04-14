# groups：当前用户组列表

TEST = {
    "order": 87,
    "name": "busybox_groups",
    "cmd": "busybox groups 2>&1",
    "expected_substring": "root",
    "expect_non_empty": True,
    "timeout": 2.0,
}
