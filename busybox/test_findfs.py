# findfs：帮助输出（避免依赖真实 LABEL/UUID）

TEST = {
    "order": 76,
    "name": "busybox_findfs",
    "cmd": "busybox findfs -h 2>&1",
    "expected_substring": "Usage: findfs",
    "expect_non_empty": True,
    "timeout": 2.0,
}
