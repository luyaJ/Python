# os.walk() 目录下所有文件输出
import os


def main():
    fileDir = "F:" + os.sep + "aaa"
    for root, dirs, files in os.walk(fileDir):
        print(root)
        print(dirs)
        print(files)
        print("\n")
        # os.system("pause")


main()
