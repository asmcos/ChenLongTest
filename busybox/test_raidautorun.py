# raidautorun：无阵列时多为错误/用法

TEST = {
    "order": 200,
    "name": "busybox_raidautorun",
    "cmd": "busybox raidautorun -h 2>&1",
    "expected_substring": "Usage: raidautorun",
    "expect_non_empty": True,
    "timeout": 2.0,
}
