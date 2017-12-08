from time import ctime, sleep as sl
from random import randint

from operator import add, mul
from functools import partial


def tsfunc(func):
    def wrappedFunc():
        print(ctime(), func.__name__)
        return func()

    return wrappedFunc


@tsfunc
def foo():
    pass


#
# foo()
# sleep(2)
# for i in range(2):
#     sleep(1)
#     foo()


def foo1():
    print("foo1 exec")


str = foo1

str()


def bar(func):
    func()


bar(foo1)


def convert(func, seq):
    return [func(x) for x in seq]


myseq = (212, 23, -32.123123, 5555, -3.2e8)

print(convert(int, myseq))


# 位置参数
def func1(a):
    print(a)


# 默认参数
def func2(a, b=1, c=3):
    print(a + b + c)


# 可变参数
def func3(a, *b):
    print(a)
    [print(x) for x in b]


func3(1, 2, 3)


# 关键字变量参数(最后一个参数是字典)
def func4(arg1, arg2='default', **arg3):
    print(arg1)
    print(arg2)
    [print(x) for x in arg3]


func4(2, c=123, d='poe')


def func5(arg1, *b, **arg3):
    print(arg1)
    [print(x) for x in b]
    [print(arg3[x]) for x in arg3]


func5(1, 2, 3, 4, 5, 6, a=243, b='43fd', c='af')

func5(2, 4, *(6, 8), **{'foo': 10, 'bar': 12})
aTuple = (6, 7, 8)
aDict = {'z': 9}
func5(1, 2, 3, x=4, y=5, *aTuple, **aDict)


def add(x, y): return x + y


add1 = lambda x, y: x + y

print(add1(2, 3))


def odd(n):
    return n % 2


allnums = []
for each in range(9):
    allnums.append(randint(1, 99))

[print(x) for x in filter(odd, allnums)]
[print(x) for x in filter(lambda x: x % 2, allnums)]
[print(x) for x in allnums if x % 2]

print(map((lambda x: x + 2), [0, 1, 2, 3, 4, 5]))
print(map((lambda x: x ** 2), range(6)))
[print(x ** 2) for x in range(6)]

[print(x) for x in zip([1, 3, 5], [2, 4, 6])]

# print(reduce((lambda x,y: x+y), range(5)))
# 偏函数
add10 = partial(add, 10)
mul10 = partial(mul, 10)
print(add10(100))
print(mul10(10))

baseTwo = partial(int, base=2)
print(baseTwo('10010'))
