# rdev：打印 root 设备号（老工具，无参时多为用法/错误）

TEST = {
    "order": 202,
    "name": "busybox_rdev",
    "cmd": "busybox rdev -h 2>&1",
    "expected_substring": "Usage: rdev",
    "expect_non_empty": True,
    "timeout": 2.0,
}
