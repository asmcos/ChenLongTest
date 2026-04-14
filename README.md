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

```bash
python3 main.py
```

日志默认写入项目下的 `logs/` 目录。
