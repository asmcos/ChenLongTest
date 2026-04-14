# mknod：无参时多为用法（不向 /dev 乱建节点）

TEST = {
    "order": 153,
    "name": "busybox_mknod",
    "cmd": "busybox mknod -h 2>&1",
    "expected_substring": "Usage: mknod",
    "expect_non_empty": True,
    "timeout": 2.0,
}
