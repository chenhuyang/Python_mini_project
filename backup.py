#!/Anaconda3/python.exe
# -*- coding:utf-8 -*-

#导入模块
import tkinter
import os
import time

#定义一个备份文件的函数
def backup():
    global entry_source
    global entry_target
    source = entry_source.get()
    target_dir = entry_target.get()

    today_dir = target_dir + time.strftime('%Y%m%d')
    time_dir = time.strftime('%H%M%S')

    touch = today_dir + os.sep + time_dir + '.zip'
    command_touch = 'zip -qr ' + touch + ' ' + source

    print(command_touch)
    print(source)
    print(target_dir)

    if os.path.exists(today_dir)==0:
        os.mkdir(today_dir)
    if os.system(command_touch)==0:
        print('Successfully backup files')
    else:
        print('Failed to backup files')

#编写图形化界面
root = tkinter.Tk()
root.title('Backup')
root.geometry('200x200')
#第一行的两个控件
lbl_source = tkinter.Label(root, text='source')
lbl_source.grid(row=0,column=0)
entry_source = tkinter.Entry(root)
entry_source.grid(row=0,column=1)
#第二行的两个控件
lbl_target = tkinter.Label(root, text='target')
lbl_target.grid(row=1,column=0)
entry_target = tkinter.Entry(root)
entry_target.grid(row=1,column=1)
#第三行的两个控件
but_back = tkinter.Button(root, text='BackUp')
but_back.grid(row=3,column=0)
but_back["command"] = backup
root.mainloop()
