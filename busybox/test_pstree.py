# pstree：进程树

TEST = {
    "order": 197,
    "name": "busybox_pstree",
    "cmd": "busybox pstree 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 2.0,
}
