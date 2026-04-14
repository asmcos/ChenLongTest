# sh：非交互执行

TEST = {
    "order": 229,
    "name": "busybox_sh",
    "cmd": "busybox sh -c 'echo sh_ok' 2>&1",
    "expected_substring": "sh_ok",
    "expect_non_empty": True,
    "timeout": 2.0,
}
