# arping：应能发送 ARP 探测（当前环境不支持时应 FAIL，暴露网络栈能力缺失）

TEST = {
    "order": 10,
    "name": "busybox_arping",
    "cmd": "busybox arping -c 1 127.0.0.1 2>&1",
    "expected_substring": "Received",
    "expect_non_empty": True,
    "timeout": 5.0,
}
