# less：无参时通常提示用法（避免交互翻页）

TEST = {
    "order": 124,
    "name": "busybox_less",
    "cmd": "busybox less 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 2.0,
}
