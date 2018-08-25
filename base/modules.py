#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'no have module note'
__author__ = 'pillar.liang'

import sys

def _privateFunc():
    print('约定: 下划线开头的是private变量')


def test():
    if len(sys.argv) == 1:
        print('hello, world')
    elif len(sys.argv) == 2:
        print('hello, %s' % sys.argv[1])
    else:
        print('to meny argv!')


if __name__ == '__main__':
    test()
