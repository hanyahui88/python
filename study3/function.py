from time import ctime, sleep


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

