# ionice：查询/设置 IO 优先级类（无参时多为当前或提示）

TEST = {
    "order": 106,
    "name": "busybox_ionice",
    "cmd": "busybox ionice 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 2.0,
}
