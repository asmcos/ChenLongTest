# busybox_list.log：depmod 之后 — df

TEST = {
    "order": 51,
    "name": "busybox_df",
    "cmd": "busybox df 2>&1",
    "expected_substring": "Filesystem",
    "expect_non_empty": True,
    "timeout": 2.0,
}
