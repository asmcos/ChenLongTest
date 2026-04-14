# busybox_list.log：chattr 之后 — chgrp

TEST = {
    "order": 28,
    "name": "busybox_chgrp",
    "cmd": "busybox chgrp -h 2>&1",
    "expected_substring": "Usage",
    "expect_non_empty": True,
    "timeout": 2.0,
}
