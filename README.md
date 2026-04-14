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

- 串口通过 TCP 暴露在本机 `127.0.0.1:4444`，可与 `main.py` 等脚本配合使用（连接时请使用与脚本一致的地址与端口）。
- `-kernel`、`-drive` 的 `file=` 等路径请按你的构建输出目录修改。

## 自动化测试脚本

### 跑全部用例（默认）

```bash
python3 main.py
```

日志默认写入项目下的 `logs/<时间戳>/`：每个用例一份串口输出 `.log`，同目录 `run.log` 为控制台镜像（总汇报）。

### 只跑单个用例

按 **`TEST` 字典里的 `name`**（与 `run.log` 里 `Running test: <name>` 一致）：

```bash
python3 main.py --test busybox_du
# 简写
python3 main.py -t busybox_du
```

按 **`order`**（与 `busybox/TEST_COMMANDS.md` 或各 `test_*.py` 中 `order` 一致）：

```bash
python3 main.py --order 57
```

可同时指定 `--test` 与 `--order`，仅当**同一条**用例两个条件都满足时才会执行（通常用于核对名称与序号是否一致）。若筛选结果为空，脚本会报错退出（不连串口）。

查看全部已加载用例的 `order` 与 `name`，可在项目根执行：

```bash
python3 -c 'from busybox import discover_loaded_tests as d; print("\n".join("%s  %s" % (s["order"], s["name"]) for s,_ in d()))'
```
