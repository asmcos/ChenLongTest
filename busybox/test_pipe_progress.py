# pipe_progress：无参时多为用法

TEST = {
    "order": 188,
    "name": "busybox_pipe_progress",
    "cmd": "busybox pipe_progress -h 2>&1",
    "expected_substring": "Usage: pipe_progress",
    "expect_non_empty": True,
    "timeout": 2.0,
}
