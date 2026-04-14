# busybox_list.log：cryptpw 之后 — cut

TEST = {
    "order": 43,
    "name": "busybox_cut",
    "cmd": "busybox echo 'a:b:c' | busybox cut -d: -f2 2>&1",
    "expected_substring": "b",
    "expect_non_empty": True,
    "timeout": 2.0,
}
