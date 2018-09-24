# 基于python的文件备份
## 一、项目简介
### 1.1 项目介绍
系统自带的备份软件，它备份出来的文件，不容易看懂，所以我决定用Python做个简单的备份脚本程序，这样我就可以备份下我的主目录和系统文件。
### 1.2 项目知识点
* python基本语法知识
* 模块os、time相关知识
* 系统一些API
### 1.3 运行环境
* python3.6
## 二、实现基本的备份程序
我们下面会通过实际的代码脚本进行实现简单的备份程序
### 2.1 代码实现

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time

source = ["/home/shiyanlou/Code/"]
target_dir = "/home/shiyanlou/Desktop/"

target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'

zip_command = "zip -qr %s %s" %(target, ' '.join(source))

if os.system(zip_command) == 0:
    print("Successful backup")
else :
    print("Backup Failed")