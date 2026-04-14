# busybox_list.log：ash 之后 — awk

TEST = {
    "order": 12,
    "name": "busybox_awk",
    "cmd": "busybox awk 'BEGIN{print \"awk_ok\"}' 2>&1",
    "expected_substring": "awk_ok",
    "expect_non_empty": True,
    "timeout": 2.0,
}
