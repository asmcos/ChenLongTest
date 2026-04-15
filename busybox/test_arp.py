# arp：应读取邻居表（当前环境不支持时应 FAIL，暴露能力缺失）

TEST = {
    "order": 9,
    "name": "busybox_arp",
    "cmd": "busybox arp 2>&1",
    "expected_substring": "HWtype",
    "expect_non_empty": True,
    "timeout": 2.0,
}
