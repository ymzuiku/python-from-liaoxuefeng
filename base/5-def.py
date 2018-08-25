# 函数用def定义
def my_abs(x):
    # 类型判断
    if not isinstance(x, (int, float)):
        # throw 错误
        raise TypeError('bad type..!')
    if x >= 0:
        return x
    else:
        return -x


def empty():
    pass

# 多类型返回的是一个tuple


def mutilReturn(x):
    return x, x*x, x*x*x


def noReturn(x):
    x += x


def enroll(name, age=6, city='shenzheng'):
    # 有默认值的参数可以不传, 也可以不按顺序传
    print(name, age, city)


def testOption(name, age, *, city, job):
    # 这个是默认取了名字的参数, 就可以不按顺序传递, 区别于默认参数是没有默认值
    # 并且都是必须传递的
    print(city, job)


def add_end(l=[]):
    l.append('add')
    return l


def testArr(arr):
    for v in arr:
        print(v)


def testArgs(*args):
    for v in args:
        print(v)


def testKeyWord(name, age, **kw):
    print(kw)


def noname(*args, **kw):
    # args 和kw都是不需要提前约定名字的
    print(args, kw)


def all(a, b, c=0, *args, **kw):
    print(a, b, c, args, kw)


print(my_abs(100))
# print(my_abs('fdaksf'))
print(mutilReturn(2))
print(noReturn(100))
print(enroll('xiaoming'))
print(enroll('xiaoming', 20))
print(enroll('xiaoming', city='beijin'))
print(testOption('dog', 10, job=20, city=30))
print(add_end([1, 2, 3]))
print(add_end())
print(add_end())  # 内部默认参数已经成为闭包内的一个变量了,因为它是可变得类型
print(testArr(['aa', 'bb']))
print(testArgs(1, 3, 5))
print(testKeyWord('dog', 100, aa='bb', bb=100, cc='bb'))
print(noname('bb', 'cc', aa='100', dog=10))
print(all(1, 2, 'a', 'b', bb=20, cc=500))


# 递归

def fact(n):
    if n == 1:
        return 1
    return n*fact(n-1)


print(fact(5))
# print(fact(999))  # 当999次时,函数stack溢出

def face2(n):
    return fact_iter(n, 1)

def fact_iter(n, product):
    if n == 1:
        return product
    return fact_iter(n-1, n*product)


print(face2(5))
# print(face2(2000)) #未做尾递归优化
