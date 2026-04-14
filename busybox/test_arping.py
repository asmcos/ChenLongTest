# arping：当前镜像不支持 AF_PACKET，预期报 socket 协议族不支持

TEST = {
    "order": 10,
    "name": "busybox_arping",
    "cmd": "busybox arping 2>&1",
    "expected_substring": "Address family not supported",
    "expect_non_empty": True,
    "timeout": 2.0,
}
