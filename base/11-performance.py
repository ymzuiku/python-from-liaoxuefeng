from math import *


def f(a):
    return abs(cos(a)) ** 0.5 + sin(2+3*a)


i = 500000
apy = range(i)

import numpy
anp = numpy.arange(i)

# f1和f2差不多慢


# for in
def f1(a):
    res = []
    for x in a:
        res.append(f(x))
    return res


# 迭代器
def f2(a):
    return [f(x) for x in a]

# (因为生成的是生成器 f(x)函数没有执行,用list进行执行之后发现性能是一样的)
# 生成器


def f3(a):
    # 错误的写法, Iterator的函数还没执行,需要用list运行next()
    # return (f(x) for x in a)
    return list((f(x) for x in a))

# map
# (因为map也是生成的是生成器, f(x)函数没有执行, 用list进行执行之后发现性能是一样的)

def f4(a):
    # 错误的写法, Iterator的函数还没执行,需要用list运行next()
    # return map(f, a)
    return list(map(f, a))


# 正确结论, map快5%, 迭代器第二快
# 全部相差不大,浮动10%,哪个合适用哪个

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
