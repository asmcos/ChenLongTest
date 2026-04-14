# unix2dos：换行转为 CRLF

TEST = {
    "order": 276,
    "name": "busybox_unix2dos",
    "cmd": "busybox printf 'u2d\n' | busybox unix2dos 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 2.0,
}
