# expand：制表符展开（printf 需 BusyBox 支持 \t）

TEST = {
    "order": 64,
    "name": "busybox_expand",
    "cmd": "busybox printf \"a\\tb\\n\" | busybox expand 2>&1",
    "expected_substring": "a",
    "expect_non_empty": True,
    "timeout": 2.0,
}
