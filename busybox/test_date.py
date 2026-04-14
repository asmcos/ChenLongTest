# busybox_list.log：cut 之后 — date（直接取年份，避免时区/格式差异）

TEST = {
    "order": 44,
    "name": "busybox_date",
    "cmd": "busybox date +%Y 2>&1",
    "expected_substring": "20",
    "expect_non_empty": True,
    "timeout": 2.0,
}
