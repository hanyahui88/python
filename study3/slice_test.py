import decimal
import operator
import random
import string

from string import Template

arr = [1, 2, '234', 'ew']
print(arr[::-1])
print(arr[::-2])

print(slice(arr))

print(3 > 5 > 6)
# value compare
print(1 == 2)

a = 1.2
b = 1 + 0.2

# a and b is same object?  no
print(a is b)
print(a is not b)
print(a == b)

# because double and string is  immutable object
print(id(a))
print(id(b))
c = 5
d = 1 + 4
print(id(c))
print(id(d))

e = 1
f = 3

print(repr(e))
print(type(e))
print(type("dasd"))

print(e == eval(repr(e)))

print(1 / 2)
print(-1 // 2)

print(decimal.Decimal(1))

print(operator.sub(2, 3))

print(random.random)

print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)

print("-" * 40)

print("afsdfsd%d", 4)
tem = Template("there is ${a} ${b}")

print(tem.substitute(a="aa", b="bb"))

str2 = "abvhfsd"

str1 = "ak;fkds"

for i, t in enumerate(str2):
    print(i, t)

print(zip(str2, str1))

print(str(1))
print(chr(97))
print(ord("a"))

arr = ['222', 'fsdf', "fsd1", 'fsd']
arr1 = ['2221', 'fsdf1', "fsd1", 'fsd1']
print(sorted(arr))
for i in reversed(arr):
    print(i)

for i in zip(arr, arr1):
    print(i)
print(tuple(arr))

[id(x) for x in arr]

print(dir(list))