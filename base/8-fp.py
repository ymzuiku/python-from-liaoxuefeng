import functools

# fliter sorted map reduce


def is_odd(n):
    return n % 2 == 1


b = list(filter(is_odd, [1, 2, 3, 4, 5, 5, 66, 621, 3]))
print(b)


c = sorted('1232kfjdklsf')
c = sorted(['bbb', 'Acb', 'Zoo', 'cre'], key=str.lower, reverse=True)


def arr2str(s):
    def fn(a, b):
        return str(a) + str(b)
    return functools.reduce(fn, s)


print(arr2str(c))


# 返回值是函数

def conut():
    fs = []
    for i in range(1, 4):
        def f():
            return i*i
        fs.append(f)
    return fs


fs = conut()

print(fs[0]())
print(fs[1]())
print(fs[2]())

# 匿名函数

a = list(map(lambda x: x*x, [1, 2, 3, 4, 5]))
print(a)


# 装饰器
def log(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        print('%s:' % (fn.__name__))
        return fn(*args, **kw)
    return wrapper


@log
def now():
    print('2015-2')


now()

# 带参数的装饰器


def fnlog(s):
    def decorator(fn):
        def wrapper(*args, **kw):
            print('%s %s():' % (s, fn.__name__))
            return fn(*args, **kw)
        return wrapper
    return decorator


@fnlog('aa')
def now2():
    print('jfdkasfjdk')


now2()

# 偏函数, 给一个函数设置一个偏好, 用于接收**kw
int2 = functools.partial(int, base=2)

print(int2('101101010010'))
