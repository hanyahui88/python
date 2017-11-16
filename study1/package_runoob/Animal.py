# -*- coding: UTF-8 -*-
class Animal:
    '所有动物的基类'
    # 以单下划线开头的表示的是 protected 类型的变量
    _name = ''
    age = 1
    # 双下划线的表示的是私有类型(private)的变量, 只能是允许这个类本身进行访问了
    __pri = True

    def __init__(self, name, age):
        self._name = name
        self.age = age
        print '父类构造'

    def introduce(self):
        print "I'm ", self._name, "I'm", self.age, "years old"

    def setName(self, name):
        self._name = name

    def setAge(self, age):
        self.age = age


dog = Animal("旺财", 19)
print hasattr(dog, 'age')
print getattr(dog, 'age')
setattr(dog, 'age1', 23)
print dir(dog)
dog.age = 18
dog.introduce()

print Animal.__dict__
print Animal.__doc__
print Animal.__name__
print Animal.__module__
print Animal.__bases__
