import os

import zipfile
import zlib


def filetest1():
    # wb+模式seek才能从当前文档向前
    file = open("data.txt", 'wb+')
    file.write(bytes("aaaaaaaaa\n", encoding="utf-8"))
    print(file.tell())
    file.write(bytes("bbbbbb", encoding="utf-8"))
    print(file.tell())
    file.seek(8, 0)
    print(file.tell())
    file.write(bytes("ccccc\n", encoding="utf-8"))
    file.close()


def filetest2():
    path = "g:\\tmp"
    if os.path.isdir(path):
        os.chdir(path)
        if os.path.isdir("aa"):
            pass
        else:
            os.mkdir("aa")
        cwd = os.getcwd()
        [print(x) for x in os.listdir(cwd)]
        print(cwd)
        os.rmdir("aa")
    else:
        os.mkdir(path)


def filetest3():
    print(zipfile.is_zipfile("G:\\tmp\\test.7z"))


def filetest4():
    try:
        open("d:/aaa.txt", "r")
    except IOError as ex:
        print("没有找到文件", ex)


def filetest5():
    try:
        open("d:/aaa.txt", "r")
    except IOError as ex:
        print("没有找到文件", ex)
    else:
        print("exce else code")
    finally:
        print("exce finally code")


def filetest6():
    with open("data.txt", "r") as f:
        [print(x) for x in f.readlines()]


filetest6()
