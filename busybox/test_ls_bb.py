# ls：与 test_ls.py（ls_root）区分；显式 busybox ls 根目录

TEST = {
    "order": 135,
    "name": "busybox_ls_bb",
    "cmd": "busybox ls / 2>&1",
    "expected_substring": "bin",
    "expect_non_empty": True,
    "timeout": 2.0,
}
