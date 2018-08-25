from math import *


def f(a):
    return abs(cos(a)) ** 0.5 + sin(2+3*a)


i = 5000000
apy = range(i)

import numpy
anp = numpy.arange(i)

# f1和f2差不多慢
def f1(a):
    res = []
    for x in a:
        res.append(f(x))
    return res


def f2(a):
    return [f(x) for x in a]

# 第二快
def f3(a):
    return (f(x) for x in a)

# 最快
def f4(a):
    return map(f, a)




func_list = ['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8']
data_list = ['apy', 'apy', 'apy', 'anp', 'anp', 'anp', 'anp', 'anp']

import time


def runtime(fn, data):
    start = time.clock()
    fn(data)
    end = time.clock()
    print('runtime: %s seconds' % (end-start))


runtime(f1, anp)
runtime(f2, anp)
runtime(f3, anp)
runtime(f4, anp)


