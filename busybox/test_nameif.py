# nameif：按 MAC 命名网卡（无 root/配置时多为错误）

TEST = {
    "order": 164,
    "name": "busybox_nameif",
    "cmd": "busybox nameif 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 2.0,
}
