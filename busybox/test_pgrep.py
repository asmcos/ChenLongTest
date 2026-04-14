# pgrep：按名匹配进程（至少应有 init 或 sh）

TEST = {
    "order": 184,
    "name": "busybox_pgrep",
    "cmd": "busybox pgrep -l init 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 2.0,
}
