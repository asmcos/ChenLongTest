# rdev：打印 root 设备号（老工具，无参时多为用法/错误）

TEST = {
    "order": 202,
    "name": "busybox_rdev",
    "cmd": "busybox rdev 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 2.0,
}
