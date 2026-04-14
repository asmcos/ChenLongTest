# modinfo：无参或无效模块名时多为用法/错误

TEST = {
    "order": 157,
    "name": "busybox_modinfo",
    "cmd": "busybox modinfo -h 2>&1",
    "expected_substring": "Usage: modinfo",
    "expect_non_empty": True,
    "timeout": 2.0,
}
