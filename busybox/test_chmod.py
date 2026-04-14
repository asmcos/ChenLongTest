# busybox_list.log：chgrp 之后 — chmod

TEST = {
    "order": 29,
    "name": "busybox_chmod",
    "cmd": "busybox chmod -h 2>&1",
    "expected_substring": "Usage",
    "expect_non_empty": True,
    "timeout": 2.0,
}
