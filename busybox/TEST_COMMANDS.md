# BusyBox 串口测试命令一览（共 50 条）

按 `order` 执行；`expected_substring` 为 `None` 时表示只校验**输出非空**（`expect_non_empty: true`）。`addgroup` / `adduser` 为定制 `run()`，实际串口步骤见各 `test_*.py`。

| order | 文件 | name | 命令与说明 |
|------:|------|------|------------|
| 1 | `test_acpid.py` | `busybox_acpid` | `busybox acpid 2>&1`（仅要求非空） |
| 2 | `test_add_shell.py` | `busybox_add_shell` | `busybox add-shell 2>&1`（仅要求非空） |
| 3 | `test_addgroup.py` | `busybox_addgroup` | 定制：`delgroup` → `addgroup <唯一组名>` → `grep -F '<组>:' /etc/group`（校验组行存在） |
| 4 | `test_adduser.py` | `busybox_adduser` | 定制：`deluser` → `adduser -D -H <唯一用户>` → `grep -F '<用户>:' /etc/passwd`（校验 passwd 行存在） |
| 5 | `test_adjtimex.py` | `busybox_adjtimex` | `busybox adjtimex 2>&1`（仅要求非空） |
| 6 | `test_busybox_list.py` | `busybox_list` | `busybox --list`（仅要求非空） |
| 7 | `test_ls.py` | `ls_root` | `ls /`，校验输出含 `bin` |
| 8 | `test_arch.py` | `busybox_arch` | `busybox arch 2>&1`（仅要求非空） |
| 9 | `test_arp.py` | `busybox_arp` | `busybox arp 2>&1`（仅要求非空） |
| 10 | `test_arping.py` | `busybox_arping` | `busybox arping 2>&1`（仅要求非空） |
| 11 | `test_ash.py` | `busybox_ash` | `busybox ash -c 'echo ash_ok' 2>&1`，校验 `ash_ok`（避免无参进入交互 shell） |
| 12 | `test_awk.py` | `busybox_awk` | `busybox awk 'BEGIN{print "awk_ok"}' 2>&1`，校验 `awk_ok` |
| 13 | `test_base64.py` | `busybox_base64` | `busybox echo test \| busybox base64 2>&1`（仅要求非空） |
| 14 | `test_basename.py` | `busybox_basename` | `busybox basename /usr/bin/foo 2>&1`，校验 `foo` |
| 15 | `test_bbconfig.py` | `busybox_bbconfig` | `busybox bbconfig 2>&1`（仅要求非空） |
| 16 | `test_bc.py` | `busybox_bc` | `busybox echo '2+2' \| busybox bc 2>&1`，校验输出含 `4` |
| 17 | `test_beep.py` | `busybox_beep` | `busybox beep 2>&1`（仅要求非空） |
| 18 | `test_blkdiscard.py` | `busybox_blkdiscard` | `busybox blkdiscard 2>&1`（仅要求非空；无设备时多为用法/错误信息） |
| 19 | `test_blkid.py` | `busybox_blkid` | `busybox blkid -h 2>&1`，校验 `Usage` |
| 20 | `test_blockdev.py` | `busybox_blockdev` | `busybox blockdev -h 2>&1`，校验 `Usage` |
| 21 | `test_brctl.py` | `busybox_brctl` | `busybox brctl -h 2>&1`，校验 `Usage` |
| 22 | `test_bunzip2.py` | `busybox_bunzip2` | `busybox bunzip2 -h 2>&1`，校验 `Usage` |
| 23 | `test_bzcat.py` | `busybox_bzcat` | `busybox bzcat -h 2>&1`，校验 `Usage` |
| 24 | `test_bzip2.py` | `busybox_bzip2` | `busybox bzip2 -h 2>&1`，校验 `Usage` |
| 25 | `test_cal.py` | `busybox_cal` | `busybox cal 2>&1`（仅要求非空） |
| 26 | `test_cat.py` | `busybox_cat` | `busybox cat /proc/version 2>&1`，校验输出含 `Linux` |
| 27 | `test_chattr.py` | `busybox_chattr` | `busybox chattr -h 2>&1`，校验 `Usage` |
| 28 | `test_chgrp.py` | `busybox_chgrp` | `busybox chgrp -h 2>&1`，校验 `Usage` |
| 29 | `test_chmod.py` | `busybox_chmod` | `busybox chmod -h 2>&1`，校验 `Usage` |
| 30 | `test_chown.py` | `busybox_chown` | `busybox chown -h 2>&1`，校验 `Usage` |
| 31 | `test_chpasswd.py` | `busybox_chpasswd` | `busybox chpasswd -h 2>&1`，校验 `Usage` |
| 32 | `test_chroot.py` | `busybox_chroot` | `busybox chroot -h 2>&1`，校验 `Usage` |
| 33 | `test_chvt.py` | `busybox_chvt` | `busybox chvt -h 2>&1`，校验 `Usage` |
| 34 | `test_cksum.py` | `busybox_cksum` | `busybox cksum /proc/version 2>&1`（仅要求非空） |
| 35 | `test_clear.py` | `busybox_clear` | `busybox clear -h 2>&1`，校验 `Usage`（清屏本身常无 stdout） |
| 36 | `test_cmp.py` | `busybox_cmp` | `busybox cmp -h 2>&1`，校验 `Usage` |
| 37 | `test_comm.py` | `busybox_comm` | `busybox comm -h 2>&1`，校验 `Usage` |
| 38 | `test_cp.py` | `busybox_cp` | `busybox cp -h 2>&1`，校验 `Usage` |
| 39 | `test_cpio.py` | `busybox_cpio` | `busybox cpio -h 2>&1`，校验 `Usage` |
| 40 | `test_crond.py` | `busybox_crond` | `busybox crond -h 2>&1`，校验 `Usage` |
| 41 | `test_crontab.py` | `busybox_crontab` | `busybox crontab -h 2>&1`，校验 `Usage` |
| 42 | `test_cryptpw.py` | `busybox_cryptpw` | `busybox cryptpw -h 2>&1`，校验 `Usage` |
| 43 | `test_cut.py` | `busybox_cut` | `echo 'a:b:c' \| cut -d: -f2`，校验输出含 `b` |
| 44 | `test_date.py` | `busybox_date` | `busybox date 2>&1`（仅要求非空） |
| 45 | `test_dc.py` | `busybox_dc` | `echo '2 2 + p' \| dc`（RPN），校验输出含 `4` |
| 46 | `test_dd.py` | `busybox_dd` | `busybox dd -h 2>&1`，校验 `Usage`（避免无参 dd） |
| 47 | `test_deallocvt.py` | `busybox_deallocvt` | `busybox deallocvt -h 2>&1`，校验 `Usage` |
| 48 | `test_delgroup.py` | `busybox_delgroup` | `busybox delgroup -h 2>&1`，校验 `Usage`（与 addgroup 定制用例不同） |
| 49 | `test_deluser.py` | `busybox_deluser` | `busybox deluser -h 2>&1`，校验 `Usage`（与 adduser 定制用例不同） |
| 50 | `test_depmod.py` | `busybox_depmod` | `busybox depmod -h 2>&1`，校验 `Usage` |

## 设计说明（简要）

- **顺序**：与 `busybox --list` 导出顺序大致对齐；中间插入 `busybox_list`、`ls_root`；前 5 个 applet 中 `addgroup` / `adduser` 用多步校验文件系统结果。
- **`-h` + `Usage`**：对可能无输出或环境相关的工具（如 `blkid`、`blockdev`、压缩类），用帮助输出做稳定断言；若你机上的 BusyBox 帮助文案不含 `Usage`，请改 `expected_substring` 为实际子串。
- **交互风险**：`ash` 使用 `-c`；`adduser` 默认 `-D -H` 避免密码交互（详见 `test_adduser.py` 注释）。
