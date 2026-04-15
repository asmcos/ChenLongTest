# busybox_list.log：awk 之后 — base64
#
# 与串口上手敲一致：`busybox echo test | busybox base64` → dGVzdAo=
# harness.send_cmd(wait_for=...) 可避免过早结束。若前面用例把会话留在非 sh（如 acpid
# 占前台），也会像「管道无效」；见 main 里每测后的 recover_shell()。
# 若 TCP 仍不转发真实 stdout，连接后 probe（busybox id 含 uid=）会告警。

TEST = {
    "order": 13,
    "name": "busybox_base64",
    "cmd": "busybox echo test | busybox base64",
    "expected_substring": "dGVzdAo=",
    "wait_for": "dGVzdAo=",
    "expect_non_empty": True,
    "timeout": 8.0,
}
