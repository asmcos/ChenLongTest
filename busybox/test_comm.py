# busybox_list.log：cmp 之后 — comm（构造两份排序文件比较）

TEST = {
    "order": 37,
    "name": "busybox_comm",
    "cmd": "busybox sh -c 'busybox printf \"a\\nb\\n\" > /tmp/bb_comm_1 && busybox printf \"b\\nc\\n\" > /tmp/bb_comm_2 && busybox comm /tmp/bb_comm_1 /tmp/bb_comm_2' 2>&1",
    "clean": "busybox sh -c 'busybox rm -f /tmp/bb_comm_1 /tmp/bb_comm_2' 2>&1",
    "expected_substring": "c",
    "expect_non_empty": True,
    "timeout": 4.0,
}
