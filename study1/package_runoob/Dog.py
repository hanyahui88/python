# -*- coding: UTF-8 -*-
from Animal import Animal


class Dog(Animal):
    # 私有变量 两个下划线开头，声明该属性为私有
    __fur = True

    def __init__(self, name, age):
        Animal.__init__(self, name, age)
        print('子类构造')

    # 在类的内部，使用 def 关键字可以为类定义一个方法，与一般函数定义不同，类方法必须包含参数 self,且为第一个参数
    def bark(self):
        print("I'm a dog")

    # 两个下划线开头，声明该方法为私有方法，不能在类地外部调用。在类的内部调用 self.__eat
    def __eat(self):
        print('我要吃饭了')


dog = Dog("name", 18)
dog.bark()
