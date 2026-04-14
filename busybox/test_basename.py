# busybox_list.log：base64 之后 — basename

TEST = {
    "order": 14,
    "name": "busybox_basename",
    "cmd": "busybox basename /usr/bin/foo 2>&1",
    "expected_substring": "foo",
    "expect_non_empty": True,
    "timeout": 2.0,
}
