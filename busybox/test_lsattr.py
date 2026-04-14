# lsattr：扩展属性列表（非 ext 上可能报错，有输出即可）

TEST = {
    "order": 136,
    "name": "busybox_lsattr",
    "cmd": "busybox lsattr -d /tmp 2>&1; busybox echo lsattr_ok",
    "expected_substring": "lsattr_ok",
    "expect_non_empty": True,
    "timeout": 2.0,
}
