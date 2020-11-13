# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: test9.py
@time: 2020/11/13 9:49
@desc:
"""
import json


def main():
    data = {
        'name': None,
        'age': True,
        'gender': False

    }
    str1 = json.dumps(data)
    print(str1)

    dict2 = json.loads(str1)
    print(dict2)


if __name__ == '__main__':
    main()
