import math


def add(*num):
    total = 0
    for i in num:
        total += i
    return total


def fabs(num):
    return math.fabs(num)
