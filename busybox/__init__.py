"""
BusyBox 子测试：每个 applet 一个模块，导出统一的 TEST 字典。
由 discover_test_specs() 动态发现并排序后交给 main 构建 TestCase。
"""

from __future__ import annotations

import importlib
import pkgutil
from typing import Any, Dict, List


def discover_test_specs() -> List[Dict[str, Any]]:
    """动态 import busybox.test_* 模块，收集 TEST 字典，按 order 排序。"""
    specs: List[Dict[str, Any]] = []
    package = __name__

    for info in pkgutil.iter_modules(__path__, prefix=f"{package}."):
        modname = info.name
        if not modname.rpartition(".")[2].startswith("test_"):
            continue
        mod = importlib.import_module(modname)
        spec = getattr(mod, "TEST", None)
        if not isinstance(spec, dict):
            continue
        if "name" not in spec or "cmd" not in spec:
            continue
        specs.append(spec)

    def sort_key(s: Dict[str, Any]) -> tuple:
        return (int(s.get("order", 9999)), s["name"])

    return sorted(specs, key=sort_key)
