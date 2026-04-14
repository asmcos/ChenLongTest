# busybox_list.log：delgroup 之后 — deluser（先增用户再删除并校验）

TEST = {
    "order": 49,
    "name": "busybox_deluser",
    "cmd": "busybox sh -c 'U=bb_delu_t && busybox deluser \"$U\" 2>/dev/null || true && busybox adduser -D -H \"$U\" && busybox deluser \"$U\" && ! busybox grep -F \"$U:\" /etc/passwd >/dev/null && busybox echo deluser_ok' 2>&1",
    "clean": "busybox sh -c 'busybox deluser bb_delu_t 2>/dev/null || true; busybox delgroup bb_delu_t 2>/dev/null || true' 2>&1",
    "expected_substring": "deluser_ok",
    "expect_non_empty": True,
    "timeout": 4.0,
}
