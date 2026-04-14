# busybox_list.log：basename 之后 — bbconfig

TEST = {
    "order": 15,
    "name": "busybox_bbconfig",
    "cmd": "busybox bbconfig 2>&1",
    "expected_substring": "CONFIG_BUSYBOX=y",
    "expect_non_empty": True,
    "timeout": 2.0,
}
