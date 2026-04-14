"""
addgroup：定制流程 —— 创建测试组并校验 /etc/group。

BusyBox 无参数时只打印 Usage；本测试带组名执行。
若将来需要交互（极少见），可用 client.read_until("提示词") + client.send_line("输入")。
"""

from __future__ import annotations

import time
from typing import Tuple

from harness import QemuSerialClient

# 每次进程内唯一组名，避免与历史残留冲突
_GROUP = f"starry_g_{int(time.time()) % 1_000_000}"

TEST = {
    "order": 3,
    "name": "busybox_addgroup",
    "cmd": f"busybox addgroup {_GROUP}; grep /etc/group (group {_GROUP})",
    "timeout": 5.0,
}


def run(client: QemuSerialClient) -> Tuple[bool, str, str]:
    g = _GROUP
    chunks: list[str] = []
    ok = False
    msg = ""
    try:
        client.send_cmd(f"busybox delgroup {g} 2>&1", timeout=2.0)

        out = client.send_cmd(f"busybox addgroup {g} 2>&1", timeout=3.0)
        chunks.append("=== busybox addgroup ===\n" + out)

        verify = client.send_cmd(f"busybox grep -F '{g}:' /etc/group 2>&1", timeout=2.0)
        chunks.append("=== grep /etc/group ===\n" + verify)

        ok = bool(verify.strip()) and (f"{g}:" in verify)
        msg = f"group line present for {g}" if ok else f"no line for {g}, got: {verify[:200]!r}"
    finally:
        try:
            cleanup = client.send_cmd(f"busybox delgroup {g} 2>&1", timeout=2.0)
            chunks.append("=== cleanup delgroup ===\n" + cleanup)
        except Exception as e:
            chunks.append(f"=== cleanup delgroup exception ===\n{e}")
    return ok, msg, "\n\n".join(chunks)
