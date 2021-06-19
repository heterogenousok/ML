#!/usr/bin/python
# author luke

import os
import time

#时间格式有三种
#一种是 秒数time.time()
#一种是字符串时间

print(os.stat('Readme').st_size)
print(os.stat('Readme').st_ino)
print(hex(os.stat('Readme').st_mode))
print(os.stat('Readme').st_uid)
print(os.stat('Readme').st_gid)
print(os.stat('Readme').st_mtime)
print(time.ctime(os.stat('Readme').st_mtime))

file=open('Readme','r+')
os.ftruncate(file.fileno(),1000)