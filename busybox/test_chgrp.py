# busybox_list.log：chattr 之后 — chgrp（创建文件并修改组，ls -ln 校验）

TEST = {
    "order": 28,
    "name": "busybox_chgrp",
    "cmd": "busybox sh -c 'busybox echo g > /tmp/bb_chgrp_t && G=$(busybox id -g) && busybox chgrp \"$G\" /tmp/bb_chgrp_t && busybox ls -ln /tmp/bb_chgrp_t | busybox grep -q \" $G \" && busybox echo chgrp_ok' 2>&1",
    "clean": "busybox sh -c 'busybox rm -f /tmp/bb_chgrp_t' 2>&1",
    "expected_substring": "chgrp_ok",
    "expect_non_empty": True,
    "timeout": 4.0,
}
