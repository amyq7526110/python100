#!/usr/bin/env python3
import tarfile

# 压缩文件的方法

tar = tarfile.open('/tmp/demo.tar.gz','w:gz') # gzip 压缩

tar.add('/etc/hosts')
tar.add('/etc/security')
tar.close()

# tar tvzf /tmp/demp.tar.gz /etc/hosts /etc/security
# 解压文件的方法
tar = tarfile.open('/tmp/demp.tar.gz','r:gz')
tar.extractall()  # 解压文件到当前目录
tar.close()
