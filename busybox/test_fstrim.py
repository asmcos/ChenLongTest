# fstrim：不对生产分区乱 trim；无参/错误路径时应有提示

TEST = {
    "order": 81,
    "name": "busybox_fstrim",
    "cmd": "busybox fstrim 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 2.0,
}
