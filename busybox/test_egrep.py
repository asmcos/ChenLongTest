# busybox_list.log：echo 之后 — egrep

TEST = {
    "order": 60,
    "name": "busybox_egrep",
    "cmd": "busybox echo hello | busybox egrep hell 2>&1",
    "expected_substring": "hello",
    "expect_non_empty": True,
    "timeout": 2.0,
}
