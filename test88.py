# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: test88.py
@time: 2020/11/12 15:54
@desc:
"""


class A:
    __BB = 3.14

    CC = 5


def main():
    a = A()
    print(A.CC)
    print(dir(a))
    print(a._A__BB)


if __name__ == '__main__':
    main()
