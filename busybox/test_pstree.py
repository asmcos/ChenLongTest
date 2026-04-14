# pstree：进程树

TEST = {
    "order": 197,
    "name": "busybox_pstree",
    "cmd": "busybox pstree 2>&1; busybox echo pstree_ok",
    "expected_substring": "pstree_ok",
    "expect_non_empty": True,
    "timeout": 2.0,
}
