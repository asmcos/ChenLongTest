# busybox_list.log：awk 之后 — base64

TEST = {
    "order": 13,
    "name": "busybox_base64",
    "cmd": "busybox echo test | busybox base64 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 2.0,
}
