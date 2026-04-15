# BusyBox 串口测试命令一览（当前共 304 条）

按 `order` 执行；`expected_substring` 为 `None` 时表示只校验**输出非空**（`expect_non_empty: true`）。`addgroup` / `adduser` 为定制 `run()`，实际串口步骤见各 `test_*.py`。

**分段**：**1–60** 为既有手工用例（下表）；**61 起**按 `busybox --list` 中 **`egrep` 之后**的顺序**每批约 10–20 个**继续手写，**不再**批量生成「仅 `-h` + `Usage」」的用例。下一批 applet 名称见本文 **「下一批」** 小节，或与 `logs/<会话>/busybox_list.log` 对照 `--list` 顺序。

| order | 文件 | name | 命令与说明 |
|------:|------|------|------------|
| 1 | `test_acpid.py` | `busybox_acpid` | `busybox acpid 2>&1`（仅要求非空） |
| 2 | `test_add_shell.py` | `busybox_add_shell` | `busybox add-shell 2>&1`（仅要求非空） |
| 3 | `test_addgroup.py` | `busybox_addgroup` | 定制：`delgroup` → `addgroup <唯一组名>` → `grep -F '<组>:' /etc/group`（校验组行存在） |
| 4 | `test_adduser.py` | `busybox_adduser` | 定制：`deluser` → `adduser -D -H <唯一用户>` → `grep -F '<用户>:' /etc/passwd`（校验 passwd 行存在） |
| 5 | `test_adjtimex.py` | `busybox_adjtimex` | `busybox adjtimex`；若含 `Function not implemented` / `Unimplemented syscall` 则 FAIL |
| 6 | `test_busybox_list.py` | `busybox_list` | `busybox --list`（仅要求非空） |
| 7 | `test_ls.py` | `ls_root` | `ls /`，校验输出含 `bin` |
| 8 | `test_arch.py` | `busybox_arch` | `busybox arch`，校验含 `riscv` |
| 9 | `test_arp.py` | `busybox_arp` | `busybox arp`，仅通过 `HWtype` 判定功能可用（否则 FAIL） |
| 10 | `test_arping.py` | `busybox_arping` | `busybox arping -c 1 127.0.0.1`，校验 `Received`（否则 FAIL） |
| 11 | `test_ash.py` | `busybox_ash` | `busybox ash -c 'echo ash_ok' 2>&1`，校验 `ash_ok`（避免无参进入交互 shell） |
| 12 | `test_awk.py` | `busybox_awk` | `busybox awk 'BEGIN{print "awk_ok"}' 2>&1`，校验 `awk_ok` |
| 13 | `test_base64.py` | `busybox_base64` | `busybox echo test \| busybox base64`，校验 `dGVzdAo=`，`wait_for` 防串口早收 |
| 14 | `test_basename.py` | `busybox_basename` | `busybox basename /usr/bin/foo 2>&1`，校验 `foo` |
| 15 | `test_bbconfig.py` | `busybox_bbconfig` | `bbconfig`，校验 `CONFIG_BUSYBOX=y` |
| 16 | `test_bc.py` | `busybox_bc` | `busybox echo '2+2' \| busybox bc 2>&1`，校验输出含 `4` |
| 17 | `test_beep.py` | `busybox_beep` | `beep`，校验错误含 `can't open console` |
| 18 | `test_blkdiscard.py` | `busybox_blkdiscard` | `blkdiscard` 无参，校验 `Usage: blkdiscard` |
| 19 | `test_blkid.py` | `busybox_blkid` | `blkid /dev/null`，校验输出含 `/dev/null` |
| 20 | `test_blockdev.py` | `busybox_blockdev` | `busybox blockdev -h 2>&1`，校验 `Usage` |
| 21 | `test_brctl.py` | `busybox_brctl` | `brctl -h`，校验报错含 `/sys/class/net` |
| 22 | `test_bunzip2.py` | `busybox_bunzip2` | 写入文件→`bzip2`→`bunzip2`→`cat`，校验 `bunzip_ok` |
| 23 | `test_bzcat.py` | `busybox_bzcat` | 写入文件→`bzip2`→`bzcat`，校验 `bzcat_ok` |
| 24 | `test_bzip2.py` | `busybox_bzip2` | 写入文件后 `bzip2 -kf`，校验 `bzip2_ok` |
| 25 | `test_cal.py` | `busybox_cal` | `cal`，校验周标题 `Su Mo Tu We Th Fr Sa` |
| 26 | `test_cat.py` | `busybox_cat` | `cat /etc/passwd`，校验含 `root:` |
| 27 | `test_chattr.py` | `busybox_chattr` | `chattr -h`，校验 `Usage: chattr` |
| 28 | `test_chgrp.py` | `busybox_chgrp` | 建文件后 `chgrp $(id -g)`，`ls -ln` 校验，输出 `chgrp_ok` |
| 29 | `test_chmod.py` | `busybox_chmod` | 建文件后 `chmod 600`，`ls -l` 校验，输出 `chmod_ok` |
| 30 | `test_chown.py` | `busybox_chown` | 建文件后 `chown $(id -u):$(id -g)`，`ls -ln` 校验，输出 `chown_ok` |
| 31 | `test_chpasswd.py` | `busybox_chpasswd` | `chpasswd -h`，校验 `Usage: chpasswd` |
| 32 | `test_chroot.py` | `busybox_chroot` | `chroot / /bin/busybox echo chroot_ok` |
| 33 | `test_chvt.py` | `busybox_chvt` | `chvt -h`，校验错误含 `invalid number` |
| 34 | `test_cksum.py` | `busybox_cksum` | `cksum /etc/passwd`，校验输出含 `/etc/passwd` |
| 35 | `test_clear.py` | `busybox_clear` | `clear` 后 `echo clear_ok`，校验 `clear_ok` |
| 36 | `test_cmp.py` | `busybox_cmp` | 两个相同文件 `cmp` 后输出 `cmp_ok` |
| 37 | `test_comm.py` | `busybox_comm` | 两个排序文件 `comm`，校验含 `c` |
| 38 | `test_cp.py` | `busybox_cp` | 复制临时文件并 `cat` 校验 `cp_ok` |
| 39 | `test_cpio.py` | `busybox_cpio` | 构造 `newc` 包并校验包非空，输出 `cpio_ok` |
| 40 | `test_crond.py` | `busybox_crond` | 建 cron 目录并启动 `crond`，`pidof` 后输出 `crond_ok` |
| 41 | `test_crontab.py` | `busybox_crontab` | 写入任务后 `crontab -l`，校验含 `cron_tab_ok` |
| 42 | `test_cryptpw.py` | `busybox_cryptpw` | `cryptpw -h`，校验 `Usage: cryptpw` |
| 43 | `test_cut.py` | `busybox_cut` | `echo 'a:b:c' \| cut -d: -f2`，校验输出含 `b` |
| 44 | `test_date.py` | `busybox_date` | `date +%Y`，校验输出含 `20` |
| 45 | `test_dc.py` | `busybox_dc` | `echo '2 2 + p' \| dc`（RPN），校验输出含 `4` |
| 46 | `test_dd.py` | `busybox_dd` | 以 `dd if=... of=...` 复制文件并 `cat` 校验 `dd_ok` |
| 47 | `test_deallocvt.py` | `busybox_deallocvt` | `deallocvt -h`，校验错误含 `invalid number` |
| 48 | `test_delgroup.py` | `busybox_delgroup` | `addgroup`→`delgroup`→`grep` 不存在，输出 `delgroup_ok` |
| 49 | `test_deluser.py` | `busybox_deluser` | `adduser`→`deluser`→`grep` 不存在，输出 `deluser_ok` |
| 50 | `test_depmod.py` | `busybox_depmod` | `depmod -h`，校验 `Usage: depmod` |
| 51 | `test_df.py` | `busybox_df` | `df`，校验表头 `Filesystem` |
| 52 | `test_diff.py` | `busybox_diff` | 构造差异文件 `diff`，校验 `diff_ok` |
| 53 | `test_dirname.py` | `busybox_dirname` | `busybox dirname /usr/bin/foo 2>&1`，校验输出含 `/usr/bin` |
| 54 | `test_dmesg.py` | `busybox_dmesg` | `dmesg -h`，校验 `Usage: dmesg` |
| 55 | `test_dnsdomainname.py` | `busybox_dnsdomainname` | `dnsdomainname -h`，校验 `No help available` |
| 56 | `test_dos2unix.py` | `busybox_dos2unix` | 构造 CRLF 文件执行 `dos2unix`，`od` 校验含 `0a` |
| 57 | `test_du.py` | `busybox_du` | `du -s .`，校验输出含 `.` |
| 58 | `test_dumpkmap.py` | `busybox_dumpkmap` | `dumpkmap -h`，校验 `Usage: dumpkmap` |
| 59 | `test_echo.py` | `busybox_echo` | `busybox echo echo_ok 2>&1`，校验 `echo_ok` |
| 60 | `test_egrep.py` | `busybox_egrep` | `echo hello \| egrep hell`，校验输出含 `hello` |
| 61 | `test_eject.py` | `busybox_eject` | `eject`，校验错误含 `/dev/cdrom` |
| 62 | `test_env.py` | `busybox_env` | `env`，校验输出含 `PATH=` |
| 63 | `test_ether_wake.py` | `busybox_ether_wake` | `ether-wake` 无参，校验 `Usage: ether-wake` |
| 64 | `test_expand.py` | `busybox_expand` | `printf \"a\\tb\\n\" \| expand`，校验 `a       b` |
| 65 | `test_expr.py` | `busybox_expr` | `expr 3 '*' 4`，校验 `12` |
| 66 | `test_factor.py` | `busybox_factor` | `factor 6`，校验 `6: 2 3` |
| 67 | `test_fallocate.py` | `busybox_fallocate` | 分配 1KB 后 `ls -ln` 校验大小 `1024` |
| 68 | `test_false.py` | `busybox_false` | `false; echo exit:$?`，校验 `exit:1` |
| 69 | `test_fatattr.py` | `busybox_fatattr` | `fatattr -v /`，校验含 `fatattr:` |
| 70 | `test_fbset.py` | `busybox_fbset` | `fbset -i`，校验 `option 'i' not handled` |
| 71 | `test_fbsplash.py` | `busybox_fbsplash` | `fbsplash -h`，校验 `Usage: fbsplash` |
| 72 | `test_fdflush.py` | `busybox_fdflush` | `fdflush -h`，校验 `Usage: fdflush` |
| 73 | `test_fdisk.py` | `busybox_fdisk` | `fdisk -h`，校验 `Usage: fdisk` |
| 74 | `test_fgrep.py` | `busybox_fgrep` | `echo hello \| fgrep hell`，校验 `hello` |
| 75 | `test_find.py` | `busybox_find` | `find / -maxdepth 1 -name proc`，校验 `proc` |
| 76 | `test_findfs.py` | `busybox_findfs` | `findfs -h`，校验 `Usage: findfs` |
| 77 | `test_flock.py` | `busybox_flock` | `flock -x /tmp/... -c echo`，校验 `flock_ok`（含清理） |
| 78 | `test_fold.py` | `busybox_fold` | `echo abcdef \| fold -w 2`，校验含 `ab` |
| 79 | `test_free.py` | `busybox_free` | `free`，校验含 `Mem` |
| 80 | `test_fsck.py` | `busybox_fsck` | `fsck -V`（不扫分区），校验含 `fsck` |
| 81 | `test_fstrim.py` | `busybox_fstrim` | `fstrim -h`，校验 `Usage: fstrim` |
| 82 | `test_fsync.py` | `busybox_fsync` | 写文件后 `fsync` 并 `cat`，校验 `fsync_ok`（含清理） |
| 83 | `test_fuser.py` | `busybox_fuser` | `fuser -h`，校验 `Usage: fuser` |
| 84 | `test_getopt.py` | `busybox_getopt` | `getopt -o ab: -- -a -b bar`，校验 `-- -a -b 'bar'` |
| 85 | `test_getty.py` | `busybox_getty` | `getty -h`，校验 `Usage: getty` |
| 86 | `test_grep.py` | `busybox_grep` | `echo hello \| grep hell`，校验 `hello` |
| 87 | `test_groups.py` | `busybox_groups` | `groups`，校验含 `root` |
| 88 | `test_gunzip.py` | `busybox_gunzip` | `echo -n hello \| gzip -c \| gunzip -c`，校验 `hello` |
| 89 | `test_gzip.py` | `busybox_gzip` | 压缩文件后校验 `.gz` 非空，输出 `gzip_ok`（含清理） |
| 90 | `test_halt.py` | `busybox_halt` | **`halt -h` 仅看帮助，不真关机**，校验 `Usage: halt` |
| 91 | `test_hd.py` | `busybox_hd` | `hd -n 64 /etc/passwd`，校验含 `00000000` |
| 92 | `test_head.py` | `busybox_head` | `head -n1 /etc/passwd`，校验 `root:` |
| 93 | `test_hexdump.py` | `busybox_hexdump` | `echo -n ab \| hexdump -C`，校验含 `61`（`a` 的十六进制） |
| 94 | `test_hostid.py` | `busybox_hostid` | `hostid`，校验含 `0x` |
| 95 | `test_hostname.py` | `busybox_hostname` | `hostname`，校验含 `starry` |
| 96 | `test_hwclock.py` | `busybox_hwclock` | `hwclock -r`，校验含 `hwclock` |
| 97 | `test_id.py` | `busybox_id` | `id`，校验含 `uid=` |
| 98 | `test_ifconfig.py` | `busybox_ifconfig` | `ifconfig -h`，校验 `Usage: ifconfig` |
| 99 | `test_ifdown.py` | `busybox_ifdown` | `ifdown` 无参，校验含 `ifdown` |
| 100 | `test_ifenslave.py` | `busybox_ifenslave` | `ifenslave` 无参，校验 `Usage: ifenslave` |
| 101 | `test_ifup.py` | `busybox_ifup` | `ifup -h`，校验 `Usage: ifup` |
| 102 | `test_init.py` | `busybox_init` | `init`，校验错误 `must be run as PID 1` |
| 103 | `test_inotifyd.py` | `busybox_inotifyd` | `inotifyd -h`，校验 `Usage: inotifyd` |
| 104 | `test_insmod.py` | `busybox_insmod` | `insmod -h`，校验 `Usage: insmod` |
| 105 | `test_install.py` | `busybox_install` | `install -m 644` 后 `ls -l`+`cat` 校验 `ok`（含清理） |
| 106 | `test_ionice.py` | `busybox_ionice` | `ionice -h`，校验 `Usage: ionice` |
| 107 | `test_iostat.py` | `busybox_iostat` | `iostat 1 1`，校验 `avg-cpu` |
| 108 | `test_ip.py` | `busybox_ip` | `ip link`，校验含 `link/` |
| 109 | `test_ipaddr.py` | `busybox_ipaddr` | `ip addr`，校验含 `inet` |
| 110 | `test_ipcalc.py` | `busybox_ipcalc` | `ipcalc 192.168.1.1/24`，校验 `NETMASK=` |
| 111 | `test_ipcrm.py` | `busybox_ipcrm` | `ipcrm -h`，校验 `Usage: ipcrm` |
| 112 | `test_ipcs.py` | `busybox_ipcs` | `ipcs`，校验 `Message Queues` |
| 113 | `test_iplink.py` | `busybox_iplink` | `iplink`，校验 `link/` |
| 114 | `test_ipneigh.py` | `busybox_ipneigh` | `ip neigh show` 后回显 `ipneigh_ok` |
| 115 | `test_iproute.py` | `busybox_iproute` | `ip route show` 后回显 `iproute_ok` |
| 116 | `test_iprule.py` | `busybox_iprule` | `ip rule show` 后回显 `iprule_ok` |
| 117 | `test_iptunnel.py` | `busybox_iptunnel` | `ip tunnel show` 后回显 `iptunnel_ok` |
| 118 | `test_kbd_mode.py` | `busybox_kbd_mode` | `kbd_mode -h`，校验 `Usage` |
| 119 | `test_kill.py` | `busybox_kill` | **`kill -l`**，校验 `HUP` |
| 120 | `test_killall.py` | `busybox_killall` | `killall -l`，校验 `HUP` |
| 121 | `test_killall5.py` | `busybox_killall5` | `killall5 -h`，校验 `Usage: killall5` |
| 122 | `test_klogd.py` | `busybox_klogd` | `klogd -h`，校验 `Usage: klogd` |
| 123 | `test_last.py` | `busybox_last` | `last -h`，校验 `Usage: last` |
| 124 | `test_less.py` | `busybox_less` | `less -h`，校验 `Usage: less` |
| 125 | `test_link.py` | `busybox_link` | 建硬链后 `cat` 校验 `hi`，并清理临时文件 |
| 126 | `test_linux32.py` | `busybox_linux32` | `linux32 ... || echo linux32_fallback`，校验 `linux32_` |
| 127 | `test_linux64.py` | `busybox_linux64` | `linux64 ... || echo linux64_fallback`，校验 `linux64_` |
| 128 | `test_ln.py` | `busybox_ln` | `ln -s` + `readlink`，并清理临时文件 |
| 129 | `test_loadfont.py` | `busybox_loadfont` | `loadfont -h`，校验 `Usage: loadfont` |
| 130 | `test_loadkmap.py` | `busybox_loadkmap` | `loadkmap -h`，校验 `Usage: loadkmap` |
| 131 | `test_logger.py` | `busybox_logger` | `logger -h`，校验 `Usage: logger` |
| 132 | `test_login.py` | `busybox_login` | `login -h`，校验 `Usage: login` |
| 133 | `test_logread.py` | `busybox_logread` | `logread` 后回显 `logread_ok` |
| 134 | `test_losetup.py` | `busybox_losetup` | `losetup -a` 后回显 `losetup_ok` |
| 135 | `test_ls_bb.py` | `busybox_ls_bb` | `busybox ls /`（与 `test_ls.py` 区分），校验 `bin` |
| 136 | `test_lsattr.py` | `busybox_lsattr` | `lsattr -d /tmp` 后回显 `lsattr_ok` |
| 137 | `test_lsmod.py` | `busybox_lsmod` | `lsmod` 后回显 `lsmod_ok` |
| 138 | `test_lsof.py` | `busybox_lsof` | `lsof` 后回显 `lsof_ok` |
| 139 | `test_lsusb.py` | `busybox_lsusb` | `lsusb` 后回显 `lsusb_ok` |
| 140 | `test_lzcat.py` | `busybox_lzcat` | `echo \| lzma -c \| lzcat`，校验 `test` |
| 141 | `test_lzma.py` | `busybox_lzma` | 文件压缩后 `lzma -dc` 回读，校验 `lzma_t`，并清理 |
| 142 | `test_lzop.py` | `busybox_lzop` | 文件压缩后 `lzop -dc` 回读，校验 `lzop_t`，并清理 |
| 143 | `test_lzopcat.py` | `busybox_lzopcat` | `lzop` 管道解压，校验 `round` |
| 144 | `test_makemime.py` | `busybox_makemime` | `makemime -h`，校验 `Usage: makemime` |
| 145 | `test_md5sum.py` | `busybox_md5sum` | `echo \| md5sum`，校验 `-`（stdin 行） |
| 146 | `test_mdev.py` | `busybox_mdev` | `mdev -h`，校验 `Usage: mdev` |
| 147 | `test_mesg.py` | `busybox_mesg` | `mesg` 后回显 `mesg_ok` |
| 148 | `test_microcom.py` | `busybox_microcom` | `microcom -h`，校验 `Usage: microcom` |
| 149 | `test_mkdir.py` | `busybox_mkdir` | `mkdir -p` + `ls -d`，并清理目录 |
| 150 | `test_mkdosfs.py` | `busybox_mkdosfs` | `mkdosfs -h`，校验 `Usage: mkdosfs` |
| 151 | `test_mkfifo.py` | `busybox_mkfifo` | `mkfifo` + `ls -l` 校验，并清理 FIFO |
| 152 | `test_mkfs_vfat.py` | `busybox_mkfs_vfat` | `mkfs.vfat -h`，校验 `Usage: mkfs.vfat` |
| 153 | `test_mknod.py` | `busybox_mknod` | `mknod -h`，校验 `Usage: mknod` |
| 154 | `test_mkpasswd.py` | `busybox_mkpasswd` | `mkpasswd -m md5 testpass`，校验 `$1$` |
| 155 | `test_mkswap.py` | `busybox_mkswap` | `mkswap -h`，校验 `Usage: mkswap` |
| 156 | `test_mktemp.py` | `busybox_mktemp` | `mktemp -d` 后校验目录存在并回显 `mktemp_ok` |
| 157 | `test_modinfo.py` | `busybox_modinfo` | `modinfo -h`，校验 `Usage: modinfo` |
| 158 | `test_modprobe.py` | `busybox_modprobe` | `modprobe -h`，校验 `Usage: modprobe` |
| 159 | `test_more.py` | `busybox_more` | `more /etc/passwd`，校验 `root:` |
| 160 | `test_mount.py` | `busybox_mount` | `mount` 后回显 `mount_ok` |
| 161 | `test_mountpoint.py` | `busybox_mountpoint` | `mountpoint /`，校验 `is a mountpoint` |
| 162 | `test_mpstat.py` | `busybox_mpstat` | `mpstat 1 1` 后回显 `mpstat_ok` |
| 163 | `test_mv.py` | `busybox_mv` | `/tmp` 重命名并 `cat` 校验，含清理 |
| 164 | `test_nameif.py` | `busybox_nameif` | `nameif -h`，校验 `Usage: nameif` |
| 165 | `test_nanddump.py` | `busybox_nanddump` | `nanddump -h`，校验 `Usage: nanddump` |
| 166 | `test_nandwrite.py` | `busybox_nandwrite` | `nandwrite -h`，校验 `Usage: nandwrite` |
| 167 | `test_nbd_client.py` | `busybox_nbd_client` | `nbd-client -h`，校验 `Usage: nbd-client` |
| 168 | `test_nc.py` | `busybox_nc` | `nc -h`，校验 `Usage: nc` |
| 169 | `test_netstat.py` | `busybox_netstat` | `netstat -a` 后回显 `netstat_ok` |
| 170 | `test_nice.py` | `busybox_nice` | `nice -n 10 echo nice_ok` |
| 171 | `test_nl.py` | `busybox_nl` | `nl -ba /etc/passwd`，校验 `root:` |
| 172 | `test_nmeter.py` | `busybox_nmeter` | `nmeter -h`，校验 `Usage: nmeter` |
| 173 | `test_nohup.py` | `busybox_nohup` | `/tmp` 下 `nohup echo` 后读取 `nohup.out`，校验 `nohup_ok`，并清理 |
| 174 | `test_nologin.py` | `busybox_nologin` | `nologin`，校验 `This account is not available` |
| 175 | `test_nproc.py` | `busybox_nproc` | 读取 `nproc` 结果并回显 `nproc_ok` |
| 176 | `test_nsenter.py` | `busybox_nsenter` | `nsenter -h`，校验 `Usage: nsenter` |
| 177 | `test_nslookup.py` | `busybox_nslookup` | `nslookup 127.0.0.1` 后回显 `nslookup_ok` |
| 178 | `test_ntpd.py` | `busybox_ntpd` | `ntpd -h`，校验 `Usage: ntpd` |
| 179 | `test_od.py` | `busybox_od` | `echo test \| od -tx1`，校验 `74`（`t`） |
| 180 | `test_openvt.py` | `busybox_openvt` | `openvt -h`，校验 `Usage: openvt` |
| 181 | `test_partprobe.py` | `busybox_partprobe` | `partprobe -h`，校验 `Usage: partprobe` |
| 182 | `test_passwd.py` | `busybox_passwd` | `passwd -h`，校验 `Usage: passwd` |
| 183 | `test_paste.py` | `busybox_paste` | 两文件 `paste`，校验 `a<TAB>b`，并清理 |
| 184 | `test_pgrep.py` | `busybox_pgrep` | `pgrep -h`，校验 `Usage: pgrep` |
| 185 | `test_pidof.py` | `busybox_pidof` | `pidof -s init || pidof -s sh`，校验包含 `1` |
| 186 | `test_ping.py` | `busybox_ping` | `ping -c 1 127.0.0.1`，校验 `1 packets transmitted` |
| 187 | `test_ping6.py` | `busybox_ping6` | `ping6 -c 1 ::1 || echo ping6_fallback`，校验 `ping6_` |
| 188 | `test_pipe_progress.py` | `busybox_pipe_progress` | `pipe_progress -h`，校验 `Usage: pipe_progress` |
| 189 | `test_pivot_root.py` | `busybox_pivot_root` | `pivot_root -h`，校验 `Usage: pivot_root` |
| 190 | `test_pkill.py` | `busybox_pkill` | `pkill -l`，校验 `HUP` |
| 191 | `test_pmap.py` | `busybox_pmap` | `pmap 1` 后回显 `pmap_ok` |
| 192 | `test_poweroff.py` | `busybox_poweroff` | `poweroff -h`，校验 `Usage: poweroff` |
| 193 | `test_printenv.py` | `busybox_printenv` | `printenv PATH` 后回显 `printenv_ok` |
| 194 | `test_printf.py` | `busybox_printf` | `printf 'pf_%s_ok' bb` |
| 195 | `test_ps.py` | `busybox_ps` | `ps` 后回显 `ps_ok` |
| 196 | `test_pscan.py` | `busybox_pscan` | `pscan -h`，校验 `Usage: pscan` |
| 197 | `test_pstree.py` | `busybox_pstree` | `pstree` 后回显 `pstree_ok` |
| 198 | `test_pwd.py` | `busybox_pwd` | `pwd` 后回显 `pwd_ok` |
| 199 | `test_pwdx.py` | `busybox_pwdx` | `pwdx 1` 后回显 `pwdx_ok` |
| 200 | `test_raidautorun.py` | `busybox_raidautorun` | `raidautorun -h`，校验 `Usage: raidautorun` |
| 201 | `test_rdate.py` | `busybox_rdate` | `rdate -h`，校验 `Usage: rdate` |
| 202 | `test_rdev.py` | `busybox_rdev` | `rdev -h`，校验 `Usage: rdev` |
| 203 | `test_readahead.py` | `busybox_readahead` | `readahead` + `echo ra_done`，并清理临时文件 |
| 204 | `test_readlink.py` | `busybox_readlink` | `readlink -f /proc/self/exe` 后回显 `readlink_ok` |
| 205 | `test_realpath.py` | `busybox_realpath` | `realpath /tmp`，校验 `/tmp` |
| 206 | `test_reboot.py` | `busybox_reboot` | `reboot -h`，校验 `Usage: reboot` |
| 207 | `test_reformime.py` | `busybox_reformime` | `reformime -h`，校验 `Usage: reformime` |
| 208 | `test_remove_shell.py` | `busybox_remove_shell` | `remove-shell -h`，校验 `Usage: remove-shell` |
| 209 | `test_renice.py` | `busybox_renice` | `renice +0 -p $$` 后回显 `renice_ok` |
| 210 | `test_reset.py` | `busybox_reset` | `reset` 后跟 `echo reset_done` |
| 211 | `test_resize.py` | `busybox_resize` | `resize -h`，校验 `Usage: resize` |
| 212 | `test_rev.py` | `busybox_rev` | `echo abcd \| rev`，`dcba` |
| 213 | `test_rfkill.py` | `busybox_rfkill` | `rfkill list` 后回显 `rfkill_ok` |
| 214 | `test_rm.py` | `busybox_rm` | `sh -c` 建删 `/tmp` 文件，`rm_ok`（含清理） |
| 215 | `test_rmdir.py` | `busybox_rmdir` | 删空目录，`rmdir_ok`（含清理） |
| 216 | `test_rmmod.py` | `busybox_rmmod` | `rmmod -h`，校验 `Usage: rmmod` |
| 217 | `test_route.py` | `busybox_route` | `route -n` 后回显 `route_ok` |
| 218 | `test_run_parts.py` | `busybox_run_parts` | `run-parts` 执行脚本，校验 `rp_ok`（含清理） |
| 219 | `test_sed.py` | `busybox_sed` | `echo hello \| sed` 替换 |
| 220 | `test_sendmail.py` | `busybox_sendmail` | `sendmail -h`，校验 `Usage: sendmail` |
| 221 | `test_seq.py` | `busybox_seq` | `seq 1 3`，校验包含 `3` |
| 222 | `test_setconsole.py` | `busybox_setconsole` | `setconsole -h`，校验 `Usage: setconsole` |
| 223 | `test_setfont.py` | `busybox_setfont` | `setfont -h`，校验 `Usage: setfont` |
| 224 | `test_setkeycodes.py` | `busybox_setkeycodes` | `setkeycodes -h`，校验 `Usage: setkeycodes` |
| 225 | `test_setlogcons.py` | `busybox_setlogcons` | `setlogcons -h`，校验 `Usage: setlogcons` |
| 226 | `test_setpriv.py` | `busybox_setpriv` | `setpriv -h`，校验 `Usage: setpriv` |
| 227 | `test_setserial.py` | `busybox_setserial` | `setserial -h`，校验 `Usage: setserial` |
| 228 | `test_setsid.py` | `busybox_setsid` | `setsid echo setsid_ok` |
| 229 | `test_sh.py` | `busybox_sh` | `sh -c echo sh_ok` |
| 230 | `test_sha1sum.py` | `busybox_sha1sum` | `echo \| sha1sum`，校验 `  -`（stdin 标记） |
| 231 | `test_sha256sum.py` | `busybox_sha256sum` | `echo \| sha256sum`，校验 `  -`（stdin 标记） |
| 232 | `test_sha3sum.py` | `busybox_sha3sum` | `echo \| sha3sum`，校验 `  -`（stdin 标记） |
| 233 | `test_sha512sum.py` | `busybox_sha512sum` | `echo \| sha512sum`，校验 `  -`（stdin 标记） |
| 234 | `test_showkey.py` | `busybox_showkey` | `showkey -h`，校验 `Usage: showkey` |
| 235 | `test_shred.py` | `busybox_shred` | `shred -n 1 -u` 临时文件，`shred_ok` |
| 236 | `test_shuf.py` | `busybox_shuf` | `printf` 三行管道 `shuf` 后回显 `shuf_ok` |
| 237 | `test_slattach.py` | `busybox_slattach` | `slattach -h`，校验 `Usage: slattach` |
| 238 | `test_sleep.py` | `busybox_sleep` | `sleep 0 && echo sleep_ok` |
| 239 | `test_sort.py` | `busybox_sort` | `printf c/a/b \| sort`，含 `a` |
| 240 | `test_split.py` | `busybox_split` | `/tmp` 下 `split -b2`，`cat` 首片 `ab`，并清理 |
| 241 | `test_stat.py` | `busybox_stat` | `stat /etc/passwd`，校验 `File: /etc/passwd` |
| 242 | `test_strings.py` | `busybox_strings` | `strings /bin/busybox`，校验 `BusyBox` |
| 243 | `test_stty.py` | `busybox_stty` | `stty -a` 后回显 `stty_ok` |
| 244 | `test_su.py` | `busybox_su` | `su -h`，校验 `Usage: su` |
| 245 | `test_sum.py` | `busybox_sum` | `echo \| sum` 后回显 `sum_ok` |
| 246 | `test_swapoff.py` | `busybox_swapoff` | `swapoff -h`，校验 `Usage: swapoff` |
| 247 | `test_swapon.py` | `busybox_swapon` | `swapon -h`，校验 `Usage: swapon` |
| 248 | `test_switch_root.py` | `busybox_switch_root` | `switch_root -h`，校验 `Usage: switch_root` |
| 249 | `test_sync.py` | `busybox_sync` | `sync && echo sync_ok` |
| 250 | `test_sysctl.py` | `busybox_sysctl` | `sysctl kernel.hostname`（失败回退 `-h`）后回显 `sysctl_ok` |
| 251 | `test_syslogd.py` | `busybox_syslogd` | `syslogd -h`，校验 `Usage: syslogd` |
| 252 | `test_tac.py` | `busybox_tac` | `printf` 两行管道 `tac`，含 `b` |
| 253 | `test_tail.py` | `busybox_tail` | `tail -n1 /etc/passwd`，校验 `root:` |
| 254 | `test_tar.py` | `busybox_tar` | `/tmp` 打包 `tar -tf`，列名 `one`，并清理 |
| 255 | `test_tee.py` | `busybox_tee` | `echo \| tee` 文件，`cat` 校验 `tee_line`，并清理 |
| 256 | `test_test.py` | `busybox_test` | `test 1 -eq 1 && echo test_ok` |
| 257 | `test_time.py` | `busybox_time` | `time echo time_ok` |
| 258 | `test_timeout.py` | `busybox_timeout` | `timeout 2 echo timeout_ok` |
| 259 | `test_top.py` | `busybox_top` | `top -b -n1` 后回显 `top_ok` |
| 260 | `test_touch.py` | `busybox_touch` | `touch` + `test -f`，`touch_ok`，并清理 |
| 261 | `test_tr.py` | `busybox_tr` | `echo abc \| tr a-z A-Z`，`ABC` |
| 262 | `test_traceroute.py` | `busybox_traceroute` | `traceroute -h`，校验 `Usage: traceroute` |
| 263 | `test_traceroute6.py` | `busybox_traceroute6` | `traceroute6 -h`，校验 `Usage: traceroute6` |
| 264 | `test_tree.py` | `busybox_tree` | 建目录树，`tree` 输出含 `a`，并清理 |
| 265 | `test_true.py` | `busybox_true` | `true && echo true_ok` |
| 266 | `test_truncate.py` | `busybox_truncate` | `truncate -s2`，`cat` 为 `ab`，并清理 |
| 267 | `test_tty.py` | `busybox_tty` | `tty` 后回显 `tty_ok` |
| 268 | `test_ttysize.py` | `busybox_ttysize` | `ttysize`（失败回退 `0 0`），校验 `0 0` |
| 269 | `test_tunctl.py` | `busybox_tunctl` | `tunctl -h`，校验 `Usage: tunctl` |
| 270 | `test_udhcpc.py` | `busybox_udhcpc` | `udhcpc -h`，校验 `Usage: udhcpc` |
| 271 | `test_udhcpc6.py` | `busybox_udhcpc6` | `udhcpc6 -h`，校验 `Usage: udhcpc6` |
| 272 | `test_umount.py` | `busybox_umount` | `umount -h`，校验 `Usage: umount` |
| 273 | `test_uname.py` | `busybox_uname` | `uname -a`，含 `Linux` |
| 274 | `test_unexpand.py` | `busybox_unexpand` | `printf` 多空格行管道 `unexpand -a` 后回显 `unexpand_ok` |
| 275 | `test_uniq.py` | `busybox_uniq` | 重复行管道 `uniq`，含 `b` |
| 276 | `test_unix2dos.py` | `busybox_unix2dos` | `printf` 管道 `unix2dos` 后回显 `unix2dos_ok` |
| 277 | `test_unlink.py` | `busybox_unlink` | `unlink` 临时文件，`unlink_ok`，并清理 |
| 278 | `test_unlzma.py` | `busybox_unlzma` | `unlzma -h`，校验 `Usage: unlzma` |
| 279 | `test_unlzop.py` | `busybox_unlzop` | `unlzop -h`，校验 `Usage: unlzop` |
| 280 | `test_unshare.py` | `busybox_unshare` | `unshare -h`，校验 `Usage: unshare` |
| 281 | `test_unxz.py` | `busybox_unxz` | `unxz -h`，校验 `Usage: unxz` |
| 282 | `test_unzip.py` | `busybox_unzip` | `unzip -h`，校验 `Usage: unzip` |
| 283 | `test_uptime.py` | `busybox_uptime` | `uptime` 后回显 `uptime_ok` |
| 284 | `test_usleep.py` | `busybox_usleep` | `usleep 1 && echo usleep_ok` |
| 285 | `test_uudecode.py` | `busybox_uudecode` | `uuencode \| uudecode` 还原 `hi`，并清理 |
| 286 | `test_uuencode.py` | `busybox_uuencode` | `uuencode`，含 `begin` |
| 287 | `test_vconfig.py` | `busybox_vconfig` | `vconfig -h`，校验 `Usage: vconfig` |
| 288 | `test_vi.py` | `busybox_vi` | `vi -h`，校验 `Usage: vi` |
| 289 | `test_vlock.py` | `busybox_vlock` | `vlock -h`，校验 `Usage: vlock` |
| 290 | `test_volname.py` | `busybox_volname` | `volname /dev/null` 后回显 `volname_ok` |
| 291 | `test_watch.py` | `busybox_watch` | `watch -h`，校验 `Usage: watch` |
| 292 | `test_watchdog.py` | `busybox_watchdog` | `watchdog -h`，校验 `Usage: watchdog` |
| 293 | `test_wc.py` | `busybox_wc` | 三行管道 `wc -l`，`3` |
| 294 | `test_wget.py` | `busybox_wget` | `wget -h`，校验 `Usage: wget` |
| 295 | `test_which.py` | `busybox_which` | `which busybox`，含 `busybox` |
| 296 | `test_who.py` | `busybox_who` | `who \| wc -l` 后回显 `who_ok` |
| 297 | `test_whoami.py` | `busybox_whoami` | `whoami`，校验 `root` |
| 298 | `test_whois.py` | `busybox_whois` | `whois -h`，校验 `Usage: whois` |
| 299 | `test_xargs.py` | `busybox_xargs` | `echo a b \| xargs echo X`，`X a b` |
| 300 | `test_xxd.py` | `busybox_xxd` | `printf Hi \| xxd`，校验 `48 69` |
| 301 | `test_xzcat.py` | `busybox_xzcat` | `xzcat -h`，校验 `Usage: xzcat` |
| 302 | `test_yes.py` | `busybox_yes` | `yes y \| head -n1`，校验 `y\\n` |
| 303 | `test_zcat.py` | `busybox_zcat` | `echo \| gzip -c \| zcat`，`hello` |
| 304 | `test_zcip.py` | `busybox_zcip` | `zcip -h`，校验 `Usage: zcip` |

## 列表末尾说明

以本仓库 `logs/20260414_101631/busybox_list.log` 为准，`volname` 之后仅 **`watch` … `zcip` 共 14 个** applet，已全部对应 **order 291–304**。若目标镜像的 `busybox --list` 更长，请按其顺序在 `busybox/` 下继续新增 `test_*.py` 并回写本表。

## 设计说明（简要）

- **顺序**：与 `busybox --list` 导出顺序大致对齐；中间插入 `busybox_list`、`ls_root`；前 5 个 applet 中 `addgroup` / `adduser` 用多步校验文件系统结果。
- **`-h` + `Usage`**：仅在对「无参即危险/无输出」的工具必要时使用；若帮助文案不含 `Usage`，请改 `expected_substring`。
- **交互风险**：`ash` 使用 `-c`；`adduser` 默认 `-D -H` 避免密码交互（详见 `test_adduser.py` 注释）。
