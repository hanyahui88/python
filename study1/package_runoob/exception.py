# -*- coding: UTF-8 -*-

try:
    1 / 0
except:
    print('exception')

try:
    fh = open("testfile", "r")
    fh.write("这是一个测试文件，用于测试异常!!")
except IOError:
    print("Error: 没有找到文件或读取文件失败")
else:
    print("内容写入文件成功")
    fh.close()

try:
    fh = open("testfile", "r")
    fh.write("这是一个测试文件，用于测试异常!!")
except (IOError, KeyError):
    print("Error: 没有找到文件或读取文件失败")
else:
    print("内容写入文件成功")
    fh.close()

try:
    1 / 0
except ZeroDivisionError:
    print('不能除以0')
finally:
    print('失败了')


def functionName(level):
    if level < 1:
        raise Exception('Invalid level!', level)


try:
    functionName(0)
except 'Invalid level':
    print('1')
else:
    print('2')
