# makemime：MIME 打包（无参时多为用法）

TEST = {
    "order": 144,
    "name": "busybox_makemime",
    "cmd": "busybox makemime 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 2.0,
}
