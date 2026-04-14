# unix2dos：换行转为 CRLF

TEST = {
    "order": 276,
    "name": "busybox_unix2dos",
    "cmd": "busybox printf 'u2d\n' | busybox unix2dos 2>&1; busybox echo unix2dos_ok",
    "expected_substring": "unix2dos_ok",
    "expect_non_empty": True,
    "timeout": 2.0,
}
