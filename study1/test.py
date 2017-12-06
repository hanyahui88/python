# -*- coding: UTF-8 -*-
import math

from mymath import add

from package_runoob.runoob1 import runoob1
from package_runoob.runoob2 import runoob2

# print(mymath.add(1,2,3,43)
# print(mymath.fabs(-4)

print(add(1, 2, 3, 43))

# 返回所有的变量和方法名
print(dir(math))
# 返回全局命名空间里的名字
print(globals())
# 返回局部命名空间里的名字
print(locals())

reload(math)

runoob1()
runoob2()

# 数从标准输入读取一个行，并返回一个字符串（去掉结尾的换行符）：
str = raw_input("请输入：");
print("你输入的内容是: ", str)

# input 可以接收一个Python表达式作为输入，并将运算结果返回。
str = input("请输入：");
print("你输入的内容是: ", str)
