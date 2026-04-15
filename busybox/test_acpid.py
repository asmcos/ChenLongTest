# busybox --list 中第 1 个 applet：acpid
#
# acpid 常以前台/守护方式占住 tty；自动化在 send_cmd 超时返回后仍可能卡在 acpid，
# 导致后续用例的输入不进 shell。main 在每测后调用 harness.recover_shell()（Ctrl-C）。

TEST = {
    "order": 1,
    "name": "busybox_acpid",
    "cmd": "busybox acpid 2>&1",
    "expected_substring": None,
    "expect_non_empty": True,
    "timeout": 2.0,
    # recover_shell 先发 Ctrl-C；仍残留时由 killall 收尾（忽略错误）
    "clean": "busybox killall acpid 2>&1; true",
}
