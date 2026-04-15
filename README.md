# ChenLongTest

StarryOS 相关自动化测试与 QEMU 启动说明。

## 启动 StarryOS（QEMU）

在启动前请根据本机环境修改内核镜像路径、磁盘镜像路径等参数。

```bash
qemu-system-riscv64 -m 1G -smp 1 -machine virt -bios default \
  -kernel /media/blx/sda2/StarryOS/StarryOS_riscv64-qemu-virt.bin \
  -device virtio-blk-pci,drive=disk0 \
  -drive id=disk0,if=none,format=raw,file=make/disk.img \
  -device virtio-net-pci,netdev=net0 \
  -netdev user,id=net0,hostfwd=tcp::5555-:5555,hostfwd=udp::5555-:5555 \
  -display none \
  -serial tcp:127.0.0.1:4444,server,nowait
```

- 串口通过 TCP 暴露在本机 `127.0.0.1:4444`，可与 `main.py` 等脚本配合使用。`main.py` 里默认连接的是 **`SERIAL_HOST`（当前为 `192.168.123.33`）与端口 `4444`**；若 QEMU 只监听本机，请用 `hostfwd` 把 `4444` 转到开发机，或直接把 `main.py` 中的 `SERIAL_HOST` 改成你的环境。
- `-kernel`、`-drive` 的 `file=` 等路径请按你的构建输出目录修改。

## 自动化测试脚本

### 跑全部用例（默认）

```bash
python3 main.py
```

日志默认写入项目下的 `logs/<时间戳>/`：每个用例一份串口输出 `.log`（文件头含 **`Order:`** 与 **`Test:`**，与 `TEST['order']` / `name` 一致，便于按序号检索），同目录 `run.log` 为控制台镜像（总汇报）；`run.log` 里每条用例也会带 **`[order N]`** 前缀。

推荐在 `TEST` 字典中按需提供 `clean` 字段，让每条用例自行清理临时产物。例如：

```python
TEST = {
    "order": 38,
    "name": "busybox_cp",
    "cmd": "busybox sh -c '...创建并验证...'",
    "clean": "busybox sh -c 'busybox rm -f /tmp/xxx /tmp/yyy' 2>&1",
    "expected_substring": "cp_ok",
    "expect_non_empty": True,
    "timeout": 4.0,
}
```

框架会在该用例执行完成后自动执行 `clean`（无论 PASS/FAIL），清理失败只记 warning，不中断主流程。

每条用例结束后、`clean` 之前，脚本会先调用 **`recover_shell()`**（连发若干次 Ctrl-C 并排空缓冲），尽量从仍占用前台的进程（例如 **`busybox acpid`**）回到交互 shell，避免后续命令的输入不进 `sh`。`acpid` 用例还带有 `clean`（`killall acpid`），与 recover 配合使用。

### 只跑部分用例（筛选）

#### 按 `name`（与 `run.log` 里 `Running test: <name>` 一致）

```bash
python3 main.py --test busybox_du
# 简写
python3 main.py -t busybox_du
```

#### 按单个 `order`（与 `busybox/TEST_COMMANDS.md` 或各 `test_*.py` 中 `order` 一致）

```bash
python3 main.py --order 57
```

#### 按 `order` 闭区间（连续一段）

```bash
python3 main.py --order-range 1-13
```

写成 `13-1` 也会自动交换为 `1-13`（闭区间）。

#### 按 `order` 列表（不连续）

逗号分隔；也支持方括号形式（整段建议加引号）：

```bash
python3 main.py --orders 1,4,6,19
python3 main.py --orders '[1,4,6,19]'
```

#### 组合与互斥

- **`--order`**、**`--order-range`**、**`--orders`** 三者**只能任选其一**。
- **`--test`** 可与上述任一方式组合：在已筛选的集合上再按 `name` 过滤（交集为空则报错退出）。

查看全部已加载用例的 `order` 与 `name`，可在项目根执行：

```bash
python3 -c 'from busybox import discover_loaded_tests as d; print("\n".join("%s  %s" % (s["order"], s["name"]) for s,_ in d()))'
```

### 排障：手敲正常、脚本 FAIL

1. **对照串口原文**：在 `starry:~#` 下试几条与用例等价的命令（管道、`&&`、`;`、`busybox` 前缀等），把**带提示符的几行原样**留下（或贴到讨论里）。对照 `logs/<会话>/busybox_*.log` 里的「串口原文」一节很有用。
2. **收包过早**：在对应 `TEST` 里加 **`wait_for`**（缓冲区出现关键子串后再按空闲结束收包），见 `harness.send_cmd`。
3. **会话不在 shell**：若上一条用例占住前台（常见为 `acpid`），表现为后续管道/输出异常；依赖每测后的 **`recover_shell()`** 与相关 `clean`。仍异常时在本机串口上手动发几次 Ctrl-C 再回到提示符后重跑。
4. **仅回显、无命令真实输出**：连接后脚本会探测 `busybox id` 是否出现 `uid=` / `gid=`。若告警而你在物理串口或别的 pty 上手动一切正常，请核对 **QEMU `-serial` 是否与自动化连接的 TCP 为同一路**；仅镜像「输入行」而不转发子进程 stdout 时，依赖子串的用例会失败。

更多命令表与约定见 `busybox/TEST_COMMANDS.md`。
