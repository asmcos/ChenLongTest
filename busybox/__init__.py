"""
BusyBox 子测试：每个 applet 一个模块，导出 TEST 字典；可选导出 run(client) 做定制流程。
无 run 时必须有 cmd；有 run 时 cmd 仅用于日志说明，可省略（将使用 [custom] name）。
"""

from __future__ import annotations

import importlib
import pkgutil
from typing import Any, Callable, Dict, List, Optional, Tuple

# 延迟类型注解：run 签名为 (QemuSerialClient) -> Tuple[bool, str, str]


def discover_loaded_tests() -> List[Tuple[Dict[str, Any], Optional[Callable]]]:
    """动态 import busybox.test_*，返回 (TEST 字典, run 或 None)，按 order 排序。"""
    loaded: List[Tuple[Dict[str, Any], Optional[Callable]]] = []
    package = __name__

    for info in pkgutil.iter_modules(__path__, prefix=f"{package}."):
        if not info.name.rpartition(".")[2].startswith("test_"):
            continue
        mod = importlib.import_module(info.name)
        spec = getattr(mod, "TEST", None)
        if not isinstance(spec, dict) or "name" not in spec:
            continue
        run_fn = getattr(mod, "run", None)
        if run_fn is None and "cmd" not in spec:
            continue
        loaded.append((spec, run_fn if callable(run_fn) else None))

    def sort_key(item: Tuple[Dict[str, Any], Optional[Callable]]) -> tuple:
        s = item[0]
        return (int(s.get("order", 9999)), s["name"])

    return sorted(loaded, key=sort_key)
