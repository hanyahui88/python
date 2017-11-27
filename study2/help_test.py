"""print method detail """
help('open')

str = "adadf"

print(str * 3)

print(str[:4])
print(str[4:])

arr = [1, 2, 4, '32']

arr1 = (2, 43, 'dg')

print(arr[3])

print(arr1)

for index, ch in enumerate(arr):
    print(index, ch)

try:
    1 / 0
except ZeroDivisionError as ex:
    print("ZeroDivisionError : {0}".format(ex))


def defaultvalue(value='hehe'):
    print("i'm {0}".format(value))


defaultvalue()
defaultvalue("heihei")

