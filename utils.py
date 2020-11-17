# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: test.py
@time: 2020/11/4 16:23
@desc:
"""
import os
import re

import pandas as pd


def delete_target_dir(target_dir: str):
    """
    清空一个路径 递归删除其下的所有文件和文件夹
    :param target_dir:
    :return:
    """
    if not os.path.exists(target_dir):
        return
    files = os.listdir(target_dir)
    for file in files:
        file = os.path.join(target_dir, file)
        if os.path.isfile(file):
            os.remove(file)
        elif os.path.isdir(file):
            delete_target_dir(file)
        else:
            print('参数错误')
    os.removedirs(target_dir)


def get_days(start: str, end: str, current_month: int) -> int:
    """
    跨月份  get_days('20200227', '20200302', 3)
    :param start:
    :param end:
    :param current_month:
    :return:
    """
    days = pd.date_range(start=start, end=end)
    targets = [pd.Timestamp(x).strftime("%Y%m%d") for x in days.values]

    if current_month > int(start[-4:-2]):
        # 跨月初
        # 找到月初第一天
        first_day = end[:-1] + '1'
        n = targets.index(first_day)
    else:
        # 跨月末
        # 找到该月最后一天 （下月最后一天 再往前推一天）
        last_day = end[:-1] + '1'
        n = targets.index(last_day) - 1

    return n


def get_split_filter_list(targets: list, prefix: str) -> list:
    results = []
    res = []
    for target in targets:
        if '\n' in target:
            results.extend(target.split('\n'))
        else:
            results.append(target)
    for result in results:
        if prefix in result:
            res.append(result)
    return list(set(res))


def get_list(targets: list, suffix: str) -> list:
    temp_list = []
    for target in targets:
        temps = str(target).rsplit(' ', 1)
        temp_list.append({temps[0]: float(str(temps[1]).replace(suffix, ''))})

    return temp_list


def get_count(mylist) -> list:
    newlist = list()

    for ml in mylist:
        for k, v in ml.items():
            res = re.search(r'.*(\d\d-\d\d) .*(\d\d-\d\d) .*', k)
            # print(res.group(1), '-->', res.group(2))
            if res.group(1) == res.group(2):
                # 同一天
                tmp = {res.group(1): v}
                newlist.append(tmp)
            else:
                # 跨天
                print('跨天处理')
                # 判断是否跨越了月份
                sd = res.group(1)
                ed = res.group(2)
                sd = int('2020' + str(sd).replace('-', ''))
                ed = int('2020' + str(ed).replace('-', ''))
                if sd < 20200901:
                    sd = 20200901
                if ed > 20200930:
                    ed = 20200930
                period = ed - sd
                ts = [sd + i for i in range(period + 1)]
                for t in ts:
                    md = str(t)[4:]
                    m_d = md[:2] + '-' + md[2:]
                    tmp = {m_d: v / (period + 1)}
                    newlist.append(tmp)
    tmp_set = set()
    for nl in newlist:
        for k in nl.keys():
            tmp_set.add(k)
    newlist2 = list()
    for tmp in tmp_set:
        nval = 0.0
        for nl in newlist:
            for k, v in nl.items():
                if tmp == k:
                    nval += v
        newlist2.append({tmp: nval})
    return newlist2


def main():
    pass


if __name__ == '__main__':
    main()
