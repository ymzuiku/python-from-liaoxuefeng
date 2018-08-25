# package
# __init__.py

import sys

def _privateFunc():
    print('约定: 下划线开头的是private变量')


def test2():
    if len(sys.argv) == 1:
        print('hello, world')
    elif len(sys.argv) == 2:
        print('hello, %s' % sys.argv[1])
    else:
        print('to meny argv!')


if __name__ == '__main__':
    test()
