# busybox_list.log：dc 之后 — dd（勿无参跑块设备；用帮助）

TEST = {
    "order": 46,
    "name": "busybox_dd",
    "cmd": "busybox dd -h 2>&1",
    "expected_substring": "Usage",
    "expect_non_empty": True,
    "timeout": 2.0,
}
