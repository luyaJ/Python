# 第一次作业：学习os.walk()用法，编写程序，统计一个给定目录下所有jpg文件的总数。输入参数，一个目录夹。输出参数，在该目录下jpg文件的总数。

import os
path = input("请输入目录地址：")
file_jpg = 0

for root, dirs, files in os.walk(path):
    print("目录地址有：", root)
    print("当前文件夹下的文件：", files, "\n")

    for file in files:
        if os.path.splitext(file)[1] == '.jpg':
            file_jpg = file_jpg + 1

print("\n该目录下jpg文件的总数为：", file_jpg)


