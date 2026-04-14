# ln：符号链接并 readlink

TEST = {
    "order": 128,
    "name": "busybox_ln",
    "cmd": "busybox rm -f /tmp/bb_ln_s && busybox echo t > /tmp/bb_ln_t && busybox ln -s /tmp/bb_ln_t /tmp/bb_ln_s && busybox readlink /tmp/bb_ln_s 2>&1",
    "expected_substring": "bb_ln_t",
    "expect_non_empty": True,
    "timeout": 2.0,
}
