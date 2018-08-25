
try:
    print(1/0)
    print('try')
except ValueError as e:
    print(2/0)
    print('except1')
except ZeroDivisionError as e:
    print('error')
    print('except2')
finally:
    print('ok')


# raise 相当于 js 的throw
def error2():
    def foo(s):
        if s == 0:
            raise ValueError('%s !== int' % s)
        return 10 / int(s)

    def bar(s):
        return foo(s) * 2

    bar(0)


# assets
# 启动Python解释器时可以用-O参数来关闭assert
# py -O
def error3():
    def foo(n):
        assert n != 5, 'n is zero!'
        return 10/n

    foo(5)


# error3()

# pdb 单步运行调试
# python -m pdb base/12-error.py (没什么用, 不如打断点)

# pdb.set_trace() 断点, 非常用有用, 但是还是没有IDE的断点好用
# 进如Pdb模式, p n 查看遍历n, c继续

import pdb

def error4():
    a = 10
    b = 90
    pdb.set_trace()
    e = b-a/10
    print(e)


# error4()


def error5():
    a = 10
    b = 90
    e = b-a/10
    print(e)

error5()