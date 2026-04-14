# busybox_list.log：bbconfig 之后 — bc

TEST = {
    "order": 16,
    "name": "busybox_bc",
    "cmd": "busybox echo '2+2' | busybox bc 2>&1",
    "expected_substring": "4",
    "expect_non_empty": True,
    "timeout": 2.0,
}
