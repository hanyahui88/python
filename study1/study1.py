# -*- coding: UTF-8 -*-
if True:
    print("ture")
else:
    print("false")
# line annotation
str = """sdf;sldkff;asldkfs;ldfksdlkfsdf
fsdfsd;lfkdsf"""

print(str)

'''
multi-line annotation
'''

"""multi-line annotation"""

import sys;

x = 'runooob';
sys.stdout.write(x + "\n")

# raw_input("\n\nPress the enter key to exit.")

x = 'a'
y = 'b'
print(x)
print(y)
print(x),
print(y),
print(x), y

counter = 100  # 赋值整型变量
miles = 1000.0  # 浮点型
name = "John"  # 字符串

print(counter)
print(miles)
print(name)

a = b = c = 1

print(a, b, c)
a, b, c = 1, 2, "john"
print(a, b, c)

str1 = "fsdfsdaaaaaaaaaaaaaaaaa"
print(str1[0])
print(str1[2:8])
print(str1[2:])

print(name * 2)
print(name + "fsfds")

# 列表

list = ['12312', '321', 'rwe', 'rwerw']
print(list[1:2])
print(list[0])
print(list * 2)
list[3] = 1.2
print(list)
# 元组，相当于只读列表
tuple = ('aa', 'fsdf', 'bb', 'ccc', 2.1)
print(tuple[1:2])
print(tuple[0])
print(tuple * 2)
# tuple[2] = 1000 #报错

dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}

print(dict['one'])  # 输出键为'one' 的值
print(dict[2])  # 输出键为 2 的值
print(tinydict)  # 输出完整的字典
print(tinydict.keys())  # 输出所有键
print(tinydict.values())  # 输出所有值

print(int(tinydict['code']))

num = 3
print(complex(num, 2))
print(repr(dict))

print(2 ** 3.0)
print(9 // 2)

a = 60  # 60 = 0011 1100
b = 13  # 13 = 0000 1101
c = 0

c = a & b;  # 12 = 0000 1100
print("1 - c 的值为：", c)

c = a | b;  # 61 = 0011 1101
print("2 - c 的值为：", c)

c = a ^ b;  # 49 = 0011 0001
print("3 - c 的值为：", c)

c = ~a;  # -61 = 1100 0011
print("4 - c 的值为：", c)

c = a << 2;  # 240 = 1111 0000
print("5 - c 的值为：", c)

a = 10
b = 20

if (a and b):
    print("1 - 变量 a 和 b 都为 true")
else:
    print("1 - 变量 a 和 b 有一个不为 true")

if (a or b):
    print("2 - 变量 a 和 b 都为 true，或其中一个变量为 true")
else:
    print("2 - 变量 a 和 b 都不为 true")

# 修改变量 a 的值
a = 0
if (a and b):
    print("3 - 变量 a 和 b 都为 true")
else:
    print("3 - 变量 a 和 b 有一个不为 true")

if (a or b):
    print("4 - 变量 a 和 b 都为 true，或其中一个变量为 true")
else:
    print("4 - 变量 a 和 b 都不为 true")

if not (a and b):
    print("5 - 变量 a 和 b 都为 false，或其中一个变量为 false")
else:
    print("5 - 变量 a 和 b 都为 true")

c = a >> 2;  # 15 = 0000 1111
print("6 - c 的值为：", c)

a = 10
b = 20
list = [1, 2, 3, 4, 5];

if (a in list):
    print("1 - 变量 a 在给定的列表中 list 中")
else:
    print("1 - 变量 a 不在给定的列表中 list 中")

if (b not in list):
    print("2 - 变量 b 不在给定的列表中 list 中")
else:
    print("2 - 变量 b 在给定的列表中 list 中")

# 修改变量 a 的值
a = 2
if (a in list):
    print("3 - 变量 a 在给定的列表中 list 中")
else:
    print("3 - 变量 a 不在给定的列表中 list 中")

a = 20
b = 20

if (a is b):
    print("1 - a 和 b 有相同的标识")
else:
    print("1 - a 和 b 没有相同的标识")

if (a is not b):
    print("2 - a 和 b 没有相同的标识")
else:
    print("2 - a 和 b 有相同的标识")

# 修改变量 b 的值
b = 30
if (a is b):
    print("3 - a 和 b 有相同的标识")
else:
    print("3 - a 和 b 没有相同的标识")

if (a is not b):
    print("4 - a 和 b 没有相同的标识")
else:
    print("4 - a 和 b 有相同的标识")

# is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等。

for letter in 'Python':  # 第一个实例
    print('当前字母 :', letter)

fruits = ['banana', 'apple', 'mango']
for fruit in fruits:  # 第二个实例
    pass
    print('这是pass块')
    print('当前水果 :', fruit)
print("Good bye!")

for index in range(len(fruits)):
    print('当前水果 :', fruits[index])
else:
    print('执行完了')

for letter in 'Python':  # 第一个实例
    if letter == 'h':
        break
    print('当期字母 :', letter)

var = 10  # 第二个实例
while var > 0:
    print('当期变量值 :', var)
    var = var - 1
    if var == 5:  # 当变量 var 等于 5 时退出循环
        break

for letter in 'Python':  # 第一个实例
    if letter == 'h':
        continue
    print('当期字母 :', letter)

print(name[1])
print("My name is %s and weight is %d kg!" % ('Zara', 21))

list = ['1', 2, 3, 54]
del list[1]
print(list)
print(len(list))
list.append("a")
print(list)
