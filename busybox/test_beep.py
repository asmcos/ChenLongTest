# busybox_list.log：bc 之后 — beep（当前镜像常返回控制台不可用）
# QEMU 虚拟机（串口/无 PC speaker 控制台）下通常只能走错误分支：can't open console。
# 这里校验的是“环境受限时的稳定报错”，不是物理蜂鸣成功。

TEST = {
    "order": 17,
    "name": "busybox_beep",
    "cmd": "busybox beep 2>&1",
    "expected_substring": "can't open console",
    "expect_non_empty": True,
    "timeout": 2.0,
}
