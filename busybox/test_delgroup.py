# busybox_list.log：deallocvt 之后 — delgroup（先增组再删除并校验）

TEST = {
    "order": 48,
    "name": "busybox_delgroup",
    "cmd": "busybox sh -c 'G=bb_delg_t && busybox delgroup \"$G\" 2>/dev/null || true && busybox addgroup \"$G\" && busybox delgroup \"$G\" && ! busybox grep -F \"$G:\" /etc/group >/dev/null && busybox echo delgroup_ok' 2>&1",
    "clean": "busybox sh -c 'busybox delgroup bb_delg_t 2>/dev/null || true' 2>&1",
    "expected_substring": "delgroup_ok",
    "expect_non_empty": True,
    "timeout": 4.0,
}
