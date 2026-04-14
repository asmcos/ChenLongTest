"""
adduser：定制流程 —— 使用 -D（不设密码）-H（不建家目录）避免交互，再查 /etc/passwd。

若必须走交互式密码，典型模式为：
  client._flush() 或先发命令
  client.send_line("busybox adduser foo")  # 视实际提示而定
  client.read_until("assword", max_total=15)   # Password/assword 兼容大小写
  client.send_line("yourpass")
  client.read_until("assword", max_total=15)   # Retype
  client.send_line("yourpass")
具体提示字符串需你在实机上抓一次串口输出再写死或放宽匹配。
"""

from __future__ import annotations

import time
from typing import Tuple

from harness import QemuSerialClient

_USER = f"starry_u_{int(time.time()) % 1_000_000}"

TEST = {
    "order": 4,
    "name": "busybox_adduser",
    "cmd": f"busybox adduser -D -H {_USER}; grep /etc/passwd (user {_USER})",
    "timeout": 5.0,
}


def run(client: QemuSerialClient) -> Tuple[bool, str, str]:
    u = _USER
    chunks: list[str] = []

    client.send_cmd(f"busybox deluser {u} 2>&1", timeout=2.0)

    out = client.send_cmd(f"busybox adduser -D -H {u} 2>&1", timeout=3.0)
    chunks.append("=== busybox adduser -D -H ===\n" + out)

    verify = client.send_cmd(f"busybox grep -F '{u}:' /etc/passwd 2>&1", timeout=2.0)
    chunks.append("=== grep /etc/passwd ===\n" + verify)

    ok = bool(verify.strip()) and (f"{u}:" in verify)
    msg = f"passwd line present for {u}" if ok else f"no line for {u}, got: {verify[:200]!r}"
    return ok, msg, "\n\n".join(chunks)
