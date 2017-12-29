# -*- coding: UTF-8 -*-
import time
import calendar

ticks = time.time()
print(ticks)

print(time.localtime(time.time()))

localtime = time.asctime(time.localtime(time.time()))
print("本地时间为 :", localtime)

# 格式化成2016-03-20 11:45:39形式
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 格式化成Sat Mar 28 22:24:24 2016形式
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))

import calendar

cal = calendar.month(2017, 11)
print("以下输出2017年11月份的日历:")
print(cal)


def printme(str):
    "打印传入的字符串到标准显示设备上"
    print(str)
    return


printme("我要调用用户自定义函数!")
printme(str="我要调用用户自定义函数!")


# 可写函数说明
def printinfo(name, age=35):
    "打印任何传入的字符串"
    print("Name: ", name);
    print("Age ", age);
    return;


# 调用printinfo函数
printinfo(age=50, name="miki");
printinfo(name="miki");


# 可写函数说明
def printinfo(arg1, *vartuple):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    for var in vartuple:
        print(var)
    return


# 调用printinfo 函数
printinfo(10);
printinfo(70, 60, 50);

sum = lambda arg1, arg2: arg1 + arg2

printme(sum(1, 2))
