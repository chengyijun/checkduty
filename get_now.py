# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: get_now.py
@time: 2020/11/12 15:21
@desc:
"""


def main():
    import time

    # 格式化成2016-03-20 11:45:39形式

    print(time.strftime("%Y", time.localtime()))


if __name__ == '__main__':
    main()
