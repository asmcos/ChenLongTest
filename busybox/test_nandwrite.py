# nandwrite：仅看帮助，勿写 NAND

TEST = {
    "order": 166,
    "name": "busybox_nandwrite",
    "cmd": "busybox nandwrite -h 2>&1",
    "expected_substring": "Usage: nandwrite",
    "expect_non_empty": True,
    "timeout": 2.0,
}
