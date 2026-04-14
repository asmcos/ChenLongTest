# BusyBox 串口测试命令一览（当前共 304 条）

按 `order` 执行；`expected_substring` 为 `None` 时表示只校验**输出非空**（`expect_non_empty: true`）。`addgroup` / `adduser` 为定制 `run()`，实际串口步骤见各 `test_*.py`。

**分段**：**1–60** 为既有手工用例（下表）；**61 起**按 `busybox --list` 中 **`egrep` 之后**的顺序**每批约 10–20 个**继续手写，**不再**批量生成「仅 `-h` + `Usage」」的用例。下一批 applet 名称见本文 **「下一批」** 小节，或与 `logs/<会话>/busybox_list.log` 对照 `--list` 顺序。

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
| 51 | `test_df.py` | `busybox_df` | `busybox df 2>&1`（仅要求非空） |
| 52 | `test_diff.py` | `busybox_diff` | `busybox diff -h 2>&1`，校验 `Usage` |
| 53 | `test_dirname.py` | `busybox_dirname` | `busybox dirname /usr/bin/foo 2>&1`，校验输出含 `/usr/bin` |
| 54 | `test_dmesg.py` | `busybox_dmesg` | `busybox dmesg -h 2>&1`，校验 `Usage` |
| 55 | `test_dnsdomainname.py` | `busybox_dnsdomainname` | `busybox dnsdomainname -h 2>&1`，校验 `Usage` |
| 56 | `test_dos2unix.py` | `busybox_dos2unix` | `busybox dos2unix -h 2>&1`，校验 `Usage` |
| 57 | `test_du.py` | `busybox_du` | `busybox du -s / 2>&1`（仅要求非空；`timeout` 3s） |
| 58 | `test_dumpkmap.py` | `busybox_dumpkmap` | `busybox dumpkmap -h 2>&1`，校验 `Usage` |
| 59 | `test_echo.py` | `busybox_echo` | `busybox echo echo_ok 2>&1`，校验 `echo_ok` |
| 60 | `test_egrep.py` | `busybox_egrep` | `echo hello \| egrep hell`，校验输出含 `hello` |
| 61 | `test_eject.py` | `busybox_eject` | `eject` 无设备时常为错误信息，仅要求非空 |
| 62 | `test_env.py` | `busybox_env` | `env`，校验输出含 `=` |
| 63 | `test_ether_wake.py` | `busybox_ether_wake` | `ether-wake` 无参，要求非空 |
| 64 | `test_expand.py` | `busybox_expand` | `printf \"a\\tb\\n\" \| expand`，校验含 `a` |
| 65 | `test_expr.py` | `busybox_expr` | `expr 3 '*' 4`，校验 `12` |
| 66 | `test_factor.py` | `busybox_factor` | `factor 6`，校验含 `2` |
| 67 | `test_fallocate.py` | `busybox_fallocate` | `/tmp` 上 `fallocate -l 0`，要求非空（成功或错误） |
| 68 | `test_false.py` | `busybox_false` | `false; echo exit:$?`，校验 `exit:1` |
| 69 | `test_fatattr.py` | `busybox_fatattr` | `fatattr -v /`，要求非空 |
| 70 | `test_fbset.py` | `busybox_fbset` | `fbset -i`，要求非空 |
| 71 | `test_fbsplash.py` | `busybox_fbsplash` | `fbsplash` 无参，要求非空 |
| 72 | `test_fdflush.py` | `busybox_fdflush` | `fdflush`，要求非空 |
| 73 | `test_fdisk.py` | `busybox_fdisk` | `fdisk -l`，要求非空（`timeout` 3s） |
| 74 | `test_fgrep.py` | `busybox_fgrep` | `echo hello \| fgrep hell`，校验 `hello` |
| 75 | `test_find.py` | `busybox_find` | `find / -maxdepth 1 -name proc`，校验 `proc` |
| 76 | `test_findfs.py` | `busybox_findfs` | `findfs` 无参，要求非空 |
| 77 | `test_flock.py` | `busybox_flock` | `flock -x /tmp/... -c echo`，校验 `flock_ok` |
| 78 | `test_fold.py` | `busybox_fold` | `echo abcdef \| fold -w 2`，校验含 `ab` |
| 79 | `test_free.py` | `busybox_free` | `free`，校验含 `Mem` |
| 80 | `test_fsck.py` | `busybox_fsck` | `fsck -V`（不扫分区），要求非空 |
| 81 | `test_fstrim.py` | `busybox_fstrim` | `fstrim` 无参，要求非空 |
| 82 | `test_fsync.py` | `busybox_fsync` | `touch` + `fsync` + `echo fsync_ok` |
| 83 | `test_fuser.py` | `busybox_fuser` | `fuser /tmp`，要求非空 |
| 84 | `test_getopt.py` | `busybox_getopt` | `getopt -o ab: -- -a -b bar`，校验含 `-a` |
| 85 | `test_getty.py` | `busybox_getty` | `getty` 无参，要求非空 |
| 86 | `test_grep.py` | `busybox_grep` | `echo hello \| grep hell`，校验 `hello` |
| 87 | `test_groups.py` | `busybox_groups` | `groups`，要求非空 |
| 88 | `test_gunzip.py` | `busybox_gunzip` | `echo -n hello \| gzip -c \| gunzip -c`，校验 `hello` |
| 89 | `test_gzip.py` | `busybox_gzip` | `echo -n hello \| gzip -c`，要求非空 |
| 90 | `test_halt.py` | `busybox_halt` | **`halt -h` 仅看帮助，不真关机**，校验 `Usage` |
| 91 | `test_hd.py` | `busybox_hd` | `hd -n 64 /proc/version` |
| 92 | `test_head.py` | `busybox_head` | `head -n1 /proc/version`，校验 `Linux` |
| 93 | `test_hexdump.py` | `busybox_hexdump` | `echo -n ab \| hexdump -C`，校验含 `61`（`a` 的十六进制） |
| 94 | `test_hostid.py` | `busybox_hostid` | `hostid`，要求非空（若空请放宽） |
| 95 | `test_hostname.py` | `busybox_hostname` | `hostname`，要求非空 |
| 96 | `test_hwclock.py` | `busybox_hwclock` | `hwclock -r`，有输出即可 |
| 97 | `test_id.py` | `busybox_id` | `id`，校验含 `uid=` |
| 98 | `test_ifconfig.py` | `busybox_ifconfig` | `ifconfig -a` |
| 99 | `test_ifdown.py` | `busybox_ifdown` | 无接口名，要求非空 |
| 100 | `test_ifenslave.py` | `busybox_ifenslave` | 无参，要求非空 |
| 101 | `test_ifup.py` | `busybox_ifup` | 无接口名，要求非空 |
| 102 | `test_init.py` | `busybox_init` | **`init -h` 仅帮助**，校验 `Usage` |
| 103 | `test_inotifyd.py` | `busybox_inotifyd` | 无参，要求非空 |
| 104 | `test_insmod.py` | `busybox_insmod` | 无参，要求非空 |
| 105 | `test_install.py` | `busybox_install` | `install` 到 `/tmp` 并 `cat` 校验 `ok` |
| 106 | `test_ionice.py` | `busybox_ionice` | `ionice`，要求非空 |
| 107 | `test_iostat.py` | `busybox_iostat` | `iostat 1 1`，`timeout` 5s |
| 108 | `test_ip.py` | `busybox_ip` | `ip link` |
| 109 | `test_ipaddr.py` | `busybox_ipaddr` | `ipaddr`（若不存在可改 `ip addr show`） |
| 110 | `test_ipcalc.py` | `busybox_ipcalc` | `ipcalc 192.168.1.1/24` |
| 111 | `test_ipcrm.py` | `busybox_ipcrm` | `ipcrm` 无参 |
| 112 | `test_ipcs.py` | `busybox_ipcs` | `ipcs` |
| 113 | `test_iplink.py` | `busybox_iplink` | `iplink` |
| 114 | `test_ipneigh.py` | `busybox_ipneigh` | `ipneigh` |
| 115 | `test_iproute.py` | `busybox_iproute` | `iproute` |
| 116 | `test_iprule.py` | `busybox_iprule` | `iprule` |
| 117 | `test_iptunnel.py` | `busybox_iptunnel` | `iptunnel` |
| 118 | `test_kbd_mode.py` | `busybox_kbd_mode` | `kbd_mode -h`，校验 `Usage` |
| 119 | `test_kill.py` | `busybox_kill` | **`kill -l`**，校验 `HUP` |
| 120 | `test_killall.py` | `busybox_killall` | **`killall -l`**（若无 `-l` 请改脚本） |
| 121 | `test_killall5.py` | `busybox_killall5` | **`killall5 -h`**，校验 `Usage` |
| 122 | `test_klogd.py` | `busybox_klogd` | **`klogd -h`**，校验 `Usage` |
| 123 | `test_last.py` | `busybox_last` | `last`（无 wtmp 可能空，可改 `-h`） |
| 124 | `test_less.py` | `busybox_less` | `less` 无参 |
| 125 | `test_link.py` | `busybox_link` | 硬链 `/tmp` 两文件，`cat` 校验 `hi` |
| 126 | `test_linux32.py` | `busybox_linux32` | `linux32 busybox echo …`，有输出即可 |
| 127 | `test_linux64.py` | `busybox_linux64` | `linux64 busybox echo linux64_ok` |
| 128 | `test_ln.py` | `busybox_ln` | `ln -s` + `readlink` |
| 129 | `test_loadfont.py` | `busybox_loadfont` | `loadfont` 无参 |
| 130 | `test_loadkmap.py` | `busybox_loadkmap` | `loadkmap` 无参 |
| 131 | `test_logger.py` | `busybox_logger` | **`logger -h`**，校验 `Usage` |
| 132 | `test_login.py` | `busybox_login` | **`login -h`**，校验 `Usage` |
| 133 | `test_logread.py` | `busybox_logread` | `logread`（可能空） |
| 134 | `test_losetup.py` | `busybox_losetup` | `losetup -a` |
| 135 | `test_ls_bb.py` | `busybox_ls_bb` | `busybox ls /`（与 `test_ls.py` 区分），校验 `bin` |
| 136 | `test_lsattr.py` | `busybox_lsattr` | `lsattr -d /tmp` |
| 137 | `test_lsmod.py` | `busybox_lsmod` | `lsmod` |
| 138 | `test_lsof.py` | `busybox_lsof` | `lsof` |
| 139 | `test_lsusb.py` | `busybox_lsusb` | `lsusb` |
| 140 | `test_lzcat.py` | `busybox_lzcat` | `echo \| lzma -c \| lzcat`，校验 `test` |
| 141 | `test_lzma.py` | `busybox_lzma` | `echo \| lzma -c`，要求非空 |
| 142 | `test_lzop.py` | `busybox_lzop` | `echo \| lzop -c`，要求非空 |
| 143 | `test_lzopcat.py` | `busybox_lzopcat` | `lzop` 管道解压，校验 `round` |
| 144 | `test_makemime.py` | `busybox_makemime` | `makemime` 无参 |
| 145 | `test_md5sum.py` | `busybox_md5sum` | `echo \| md5sum`，校验 `-`（stdin 行） |
| 146 | `test_mdev.py` | `busybox_mdev` | **`mdev -h`**，校验 `Usage` |
| 147 | `test_mesg.py` | `busybox_mesg` | `mesg` |
| 148 | `test_microcom.py` | `busybox_microcom` | `microcom` 无参 |
| 149 | `test_mkdir.py` | `busybox_mkdir` | `mkdir -p` + `ls -d` |
| 150 | `test_mkdosfs.py` | `busybox_mkdosfs` | **`mkdosfs -h`**，校验 `Usage` |
| 151 | `test_mkfifo.py` | `busybox_mkfifo` | `mkfifo` + `ls -l` |
| 152 | `test_mkfs_vfat.py` | `busybox_mkfs_vfat` | **`mkfs.vfat -h`** |
| 153 | `test_mknod.py` | `busybox_mknod` | `mknod` 无参 |
| 154 | `test_mkpasswd.py` | `busybox_mkpasswd` | `mkpasswd -m md5 testpass`，校验含 `$` |
| 155 | `test_mkswap.py` | `busybox_mkswap` | **`mkswap -h`** |
| 156 | `test_mktemp.py` | `busybox_mktemp` | `mktemp -d -t bbXXXXXX` |
| 157 | `test_modinfo.py` | `busybox_modinfo` | `modinfo` 无参 |
| 158 | `test_modprobe.py` | `busybox_modprobe` | **`modprobe -h`** |
| 159 | `test_more.py` | `busybox_more` | `more /proc/version`，校验 `Linux` |
| 160 | `test_mount.py` | `busybox_mount` | `mount` 列表 |
| 161 | `test_mountpoint.py` | `busybox_mountpoint` | `mountpoint /` |
| 162 | `test_mpstat.py` | `busybox_mpstat` | `mpstat 1 1`，`timeout` 5s |
| 163 | `test_mv.py` | `busybox_mv` | `/tmp` 重命名并 `cat` |
| 164 | `test_nameif.py` | `busybox_nameif` | `nameif` 无参 |
| 165 | `test_nanddump.py` | `busybox_nanddump` | **`nanddump -h`** |
| 166 | `test_nandwrite.py` | `busybox_nandwrite` | **`nandwrite -h`** |
| 167 | `test_nbd_client.py` | `busybox_nbd_client` | **`nbd-client -h`** |
| 168 | `test_nc.py` | `busybox_nc` | **`nc -h`**，校验 `Usage` |
| 169 | `test_netstat.py` | `busybox_netstat` | `netstat -a` |
| 170 | `test_nice.py` | `busybox_nice` | `nice -n 10 echo nice_ok` |
| 171 | `test_nl.py` | `busybox_nl` | `nl -ba /proc/version`，校验 `Linux` |
| 172 | `test_nmeter.py` | `busybox_nmeter` | **`nmeter -h`**（避免常驻刷新） |
| 173 | `test_nohup.py` | `busybox_nohup` | `/tmp` 下 `nohup echo nohup_ok` |
| 174 | `test_nologin.py` | `busybox_nologin` | `nologin` |
| 175 | `test_nproc.py` | `busybox_nproc` | `nproc` |
| 176 | `test_nsenter.py` | `busybox_nsenter` | **`nsenter -h`** |
| 177 | `test_nslookup.py` | `busybox_nslookup` | `nslookup 127.0.0.1`，`timeout` 5s |
| 178 | `test_ntpd.py` | `busybox_ntpd` | **`ntpd -h`** |
| 179 | `test_od.py` | `busybox_od` | `echo test \| od -tx1`，校验 `74`（`t`） |
| 180 | `test_openvt.py` | `busybox_openvt` | **`openvt -h`** |
| 181 | `test_partprobe.py` | `busybox_partprobe` | `partprobe` 无参 |
| 182 | `test_passwd.py` | `busybox_passwd` | **`passwd -h`** |
| 183 | `test_paste.py` | `busybox_paste` | 两文件 `paste` |
| 184 | `test_pgrep.py` | `busybox_pgrep` | `pgrep -l init` |
| 185 | `test_pidof.py` | `busybox_pidof` | `pidof init` |
| 186 | `test_ping.py` | `busybox_ping` | `ping -c 1 127.0.0.1`，`timeout` 5s |
| 187 | `test_ping6.py` | `busybox_ping6` | `ping6 -c 1 ::1`（可无 IPv6） |
| 188 | `test_pipe_progress.py` | `busybox_pipe_progress` | `pipe_progress` 无参 |
| 189 | `test_pivot_root.py` | `busybox_pivot_root` | **`pivot_root -h`** |
| 190 | `test_pkill.py` | `busybox_pkill` | **`pkill -h`** |
| 191 | `test_pmap.py` | `busybox_pmap` | `pmap 1` |
| 192 | `test_poweroff.py` | `busybox_poweroff` | **`poweroff -h`** |
| 193 | `test_printenv.py` | `busybox_printenv` | `printenv PATH` |
| 194 | `test_printf.py` | `busybox_printf` | `printf 'pf_%s_ok' bb` |
| 195 | `test_ps.py` | `busybox_ps` | `ps` |
| 196 | `test_pscan.py` | `busybox_pscan` | `pscan` 无参 |
| 197 | `test_pstree.py` | `busybox_pstree` | `pstree` |
| 198 | `test_pwd.py` | `busybox_pwd` | `pwd` |
| 199 | `test_pwdx.py` | `busybox_pwdx` | `pwdx 1` |
| 200 | `test_raidautorun.py` | `busybox_raidautorun` | `raidautorun` 无参 |
| 201 | `test_rdate.py` | `busybox_rdate` | `rdate` 无参 |
| 202 | `test_rdev.py` | `busybox_rdev` | `rdev` |
| 203 | `test_readahead.py` | `busybox_readahead` | `readahead` + `echo ra_done` |
| 204 | `test_readlink.py` | `busybox_readlink` | `readlink -f /proc/self/exe` |
| 205 | `test_realpath.py` | `busybox_realpath` | `realpath /tmp` |
| 206 | `test_reboot.py` | `busybox_reboot` | **`reboot -h`** |
| 207 | `test_reformime.py` | `busybox_reformime` | `reformime` 无参 |
| 208 | `test_remove_shell.py` | `busybox_remove_shell` | `remove-shell` 无参 |
| 209 | `test_renice.py` | `busybox_renice` | `sh -c 'renice +0 -p $$'` |
| 210 | `test_reset.py` | `busybox_reset` | `reset` 后跟 `echo reset_done` |
| 211 | `test_resize.py` | `busybox_resize` | **`resize -h`** |
| 212 | `test_rev.py` | `busybox_rev` | `echo abcd \| rev`，`dcba` |
| 213 | `test_rfkill.py` | `busybox_rfkill` | `rfkill list` |
| 214 | `test_rm.py` | `busybox_rm` | `sh -c` 建删 `/tmp` 文件，`rm_ok` |
| 215 | `test_rmdir.py` | `busybox_rmdir` | 删空目录，`rmdir_ok` |
| 216 | `test_rmmod.py` | `busybox_rmmod` | **`rmmod -h`** |
| 217 | `test_route.py` | `busybox_route` | `route -n` |
| 218 | `test_run_parts.py` | `busybox_run_parts` | `run-parts` 执行脚本，`rp_ok` |
| 219 | `test_sed.py` | `busybox_sed` | `echo hello \| sed` 替换 |
| 220 | `test_sendmail.py` | `busybox_sendmail` | **`sendmail -h`** |
| 221 | `test_seq.py` | `busybox_seq` | `seq 1 3` |
| 222 | `test_setconsole.py` | `busybox_setconsole` | **`setconsole -h`** |
| 223 | `test_setfont.py` | `busybox_setfont` | **`setfont -h`** |
| 224 | `test_setkeycodes.py` | `busybox_setkeycodes` | **`setkeycodes -h`** |
| 225 | `test_setlogcons.py` | `busybox_setlogcons` | **`setlogcons -h`** |
| 226 | `test_setpriv.py` | `busybox_setpriv` | **`setpriv -h`** |
| 227 | `test_setserial.py` | `busybox_setserial` | **`setserial -h`** |
| 228 | `test_setsid.py` | `busybox_setsid` | `setsid echo setsid_ok` |
| 229 | `test_sh.py` | `busybox_sh` | `sh -c echo sh_ok` |
| 230 | `test_sha1sum.py` | `busybox_sha1sum` | `echo \| sha1sum`，校验 `-` |
| 231 | `test_sha256sum.py` | `busybox_sha256sum` | `echo \| sha256sum`，校验 `-` |
| 232 | `test_sha3sum.py` | `busybox_sha3sum` | `echo \| sha3sum`，校验 `-` |
| 233 | `test_sha512sum.py` | `busybox_sha512sum` | `echo \| sha512sum`，校验 `-` |
| 234 | `test_showkey.py` | `busybox_showkey` | **`showkey -h`** |
| 235 | `test_shred.py` | `busybox_shred` | `shred -n 1 -u` 临时文件，`shred_ok` |
| 236 | `test_shuf.py` | `busybox_shuf` | `printf` 三行管道 `shuf`（仅要求非空） |
| 237 | `test_slattach.py` | `busybox_slattach` | **`slattach -h`** |
| 238 | `test_sleep.py` | `busybox_sleep` | `sleep 0 && echo sleep_ok` |
| 239 | `test_sort.py` | `busybox_sort` | `printf c/a/b \| sort`，含 `a` |
| 240 | `test_split.py` | `busybox_split` | `/tmp` 下 `split -b2`，`cat` 首片 `ab` |
| 241 | `test_stat.py` | `busybox_stat` | `stat /proc/version`（仅要求非空） |
| 242 | `test_strings.py` | `busybox_strings` | `strings /proc/version`，含 `Linux` |
| 243 | `test_stty.py` | `busybox_stty` | `stty -a`（仅要求非空） |
| 244 | `test_su.py` | `busybox_su` | **`su -h`** |
| 245 | `test_sum.py` | `busybox_sum` | `echo \| sum`（仅要求非空） |
| 246 | `test_swapoff.py` | `busybox_swapoff` | **`swapoff -h`** |
| 247 | `test_swapon.py` | `busybox_swapon` | **`swapon -h`** |
| 248 | `test_switch_root.py` | `busybox_switch_root` | **`switch_root -h`** |
| 249 | `test_sync.py` | `busybox_sync` | `sync && echo sync_ok` |
| 250 | `test_sysctl.py` | `busybox_sysctl` | `sysctl kernel.hostname`，失败则 **`sysctl -h`** |
| 251 | `test_syslogd.py` | `busybox_syslogd` | **`syslogd -h`** |
| 252 | `test_tac.py` | `busybox_tac` | `printf` 两行管道 `tac`，含 `b` |
| 253 | `test_tail.py` | `busybox_tail` | `tail -n1 /proc/version`，含 `Linux` |
| 254 | `test_tar.py` | `busybox_tar` | `/tmp` 打包 `tar -tf`，列名 `one` |
| 255 | `test_tee.py` | `busybox_tee` | `echo \| tee` 文件，`cat` 校验 `tee_line` |
| 256 | `test_test.py` | `busybox_test` | `test 1 -eq 1 && echo test_ok` |
| 257 | `test_time.py` | `busybox_time` | `time echo time_ok` |
| 258 | `test_timeout.py` | `busybox_timeout` | `timeout 2 echo timeout_ok` |
| 259 | `test_top.py` | `busybox_top` | **`top -b -n1`**（仅要求非空） |
| 260 | `test_touch.py` | `busybox_touch` | `touch` + `test -f`，`touch_ok` |
| 261 | `test_tr.py` | `busybox_tr` | `echo abc \| tr a-z A-Z`，`ABC` |
| 262 | `test_traceroute.py` | `busybox_traceroute` | **`traceroute -h`** |
| 263 | `test_traceroute6.py` | `busybox_traceroute6` | **`traceroute6 -h`** |
| 264 | `test_tree.py` | `busybox_tree` | 建目录树，`tree` 输出含 `a` |
| 265 | `test_true.py` | `busybox_true` | `true && echo true_ok` |
| 266 | `test_truncate.py` | `busybox_truncate` | `truncate -s2`，`cat` 为 `ab` |
| 267 | `test_tty.py` | `busybox_tty` | `tty`（仅要求非空） |
| 268 | `test_ttysize.py` | `busybox_ttysize` | `ttysize` 或回退 `0 0`（仅要求非空） |
| 269 | `test_tunctl.py` | `busybox_tunctl` | **`tunctl -h`** |
| 270 | `test_udhcpc.py` | `busybox_udhcpc` | **`udhcpc -h`** |
| 271 | `test_udhcpc6.py` | `busybox_udhcpc6` | **`udhcpc6 -h`** |
| 272 | `test_umount.py` | `busybox_umount` | **`umount -h`** |
| 273 | `test_uname.py` | `busybox_uname` | `uname -a`，含 `Linux` |
| 274 | `test_unexpand.py` | `busybox_unexpand` | `printf` 多空格行管道 `unexpand -a`（仅要求非空） |
| 275 | `test_uniq.py` | `busybox_uniq` | 重复行管道 `uniq`，含 `b` |
| 276 | `test_unix2dos.py` | `busybox_unix2dos` | `printf` 管道 `unix2dos`（仅要求非空） |
| 277 | `test_unlink.py` | `busybox_unlink` | `unlink` 临时文件，`unlink_ok` |
| 278 | `test_unlzma.py` | `busybox_unlzma` | **`unlzma -h`** |
| 279 | `test_unlzop.py` | `busybox_unlzop` | **`unlzop -h`** |
| 280 | `test_unshare.py` | `busybox_unshare` | **`unshare -h`** |
| 281 | `test_unxz.py` | `busybox_unxz` | **`unxz -h`** |
| 282 | `test_unzip.py` | `busybox_unzip` | **`unzip -h`** |
| 283 | `test_uptime.py` | `busybox_uptime` | `uptime`（仅要求非空） |
| 284 | `test_usleep.py` | `busybox_usleep` | `usleep 1 && echo usleep_ok` |
| 285 | `test_uudecode.py` | `busybox_uudecode` | `uuencode \| uudecode` 还原 `hi` |
| 286 | `test_uuencode.py` | `busybox_uuencode` | `uuencode`，含 `begin` |
| 287 | `test_vconfig.py` | `busybox_vconfig` | **`vconfig -h`** |
| 288 | `test_vi.py` | `busybox_vi` | **`vi -h`** |
| 289 | `test_vlock.py` | `busybox_vlock` | **`vlock -h`** |
| 290 | `test_volname.py` | `busybox_volname` | `volname /dev/null`（仅要求非空） |
| 291 | `test_watch.py` | `busybox_watch` | **`watch -h`** |
| 292 | `test_watchdog.py` | `busybox_watchdog` | **`watchdog -h`** |
| 293 | `test_wc.py` | `busybox_wc` | 三行管道 `wc -l`，`3` |
| 294 | `test_wget.py` | `busybox_wget` | **`wget -h`** |
| 295 | `test_which.py` | `busybox_which` | `which busybox`，含 `busybox` |
| 296 | `test_who.py` | `busybox_who` | `who \| wc -l`（仅要求非空） |
| 297 | `test_whoami.py` | `busybox_whoami` | `whoami`（仅要求非空） |
| 298 | `test_whois.py` | `busybox_whois` | **`whois -h`** |
| 299 | `test_xargs.py` | `busybox_xargs` | `echo a b \| xargs echo X`，`X a b` |
| 300 | `test_xxd.py` | `busybox_xxd` | `printf Hi \| xxd`，含 `48` |
| 301 | `test_xzcat.py` | `busybox_xzcat` | **`xzcat -h`** |
| 302 | `test_yes.py` | `busybox_yes` | `yes y \| head -n1`，含 `y` |
| 303 | `test_zcat.py` | `busybox_zcat` | `echo \| gzip -c \| zcat`，`hello` |
| 304 | `test_zcip.py` | `busybox_zcip` | **`zcip -h`** |

## 列表末尾说明

以本仓库 `logs/20260414_101631/busybox_list.log` 为准，`volname` 之后仅 **`watch` … `zcip` 共 14 个** applet，已全部对应 **order 291–304**。若目标镜像的 `busybox --list` 更长，请按其顺序在 `busybox/` 下继续新增 `test_*.py` 并回写本表。

## 设计说明（简要）

- **顺序**：与 `busybox --list` 导出顺序大致对齐；中间插入 `busybox_list`、`ls_root`；前 5 个 applet 中 `addgroup` / `adduser` 用多步校验文件系统结果。
- **`-h` + `Usage`**：仅在对「无参即危险/无输出」的工具必要时使用；若帮助文案不含 `Usage`，请改 `expected_substring`。
- **交互风险**：`ash` 使用 `-c`；`adduser` 默认 `-D -H` 避免密码交互（详见 `test_adduser.py` 注释）。
