dic = {}.fromkeys(('x', 'y'), -1)
print(dic)

for key in dic.keys():
    print(key, dic[key])
for key in dic:
    print(key, dic[key])

if 'x' in dic:
    print(dic['x'])
dict3 = {3.2: 'xyz', 1: 'abc', '1': 3.14159}
dict3[11] = 12
print(dict3)
key = dict3.pop(11)
print(key)
# del dict3[11]
print(dict3)

# dict3.clear()
# del dict3

dict4 = dict3.copy()
print(id(dict3))
print(id(dict4))
print(hash("aa"))

print(dict3.keys())
print(dict3.values())

s = set('aa')
s.add('5')
s.add('b')
s.add('90')
print(s)
ss = frozenset('bbcsdfgds')
print(ss)
print(len(ss))
