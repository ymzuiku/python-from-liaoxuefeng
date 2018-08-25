from collections import Iterable


def slice1():
    l = ['mic', 'bb', 'cc', 'dd']
    l = l[0:3]
    l = l[:2]
    print(l)


slice1()


def slice2():
    l = list(range(10))
    l = l[:-3]
    print(l)


slice2()


def slice3():
    l = list(range(20))
    # 取前10个, 每2个取1个
    l = l[:10:2]
    print(l)


slice3()


def slice4():
    l = list(range(20))
    # 每2个取1个
    l = l[::3]
    print(l)


slice4()

# 判断是否是某几个类型
print(isinstance('bb', (int, float)))

# 判断是否可迭代
print(isinstance('bbb', Iterable))

