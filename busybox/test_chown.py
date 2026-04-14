# busybox_list.log：chmod 之后 — chown（创建文件并改为当前 uid:gid，ls -ln 校验）

TEST = {
    "order": 30,
    "name": "busybox_chown",
    "cmd": "busybox sh -c 'busybox echo o > /tmp/bb_chown_t && U=$(busybox id -u) && G=$(busybox id -g) && busybox chown \"$U:$G\" /tmp/bb_chown_t && busybox ls -ln /tmp/bb_chown_t | busybox grep -q \" $U $G \" && busybox echo chown_ok' 2>&1",
    "clean": "busybox sh -c 'busybox rm -f /tmp/bb_chown_t' 2>&1",
    "expected_substring": "chown_ok",
    "expect_non_empty": True,
    "timeout": 4.0,
}
