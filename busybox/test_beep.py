# busybox_list.log：bc 之后 — beep（无参通常立即返回或报错，不长时间鸣叫）

TEST = {
    "order": 17,
    "name": "busybox_beep",
    "cmd": "busybox beep 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 2.0,
}
