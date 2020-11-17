# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: rules.py
@time: 2020/11/16 14:46
@desc:
"""
import json
import re

from openpyxl import load_workbook


def main():
    Rule()


class Rule:
    def __init__(self):
        self.write_result()

    def write_result(self):
        # 读取数据
        with open('./datas/results.json', 'r', encoding='utf-8') as f:
            results = json.load(f)

        datas = self.__get_results_by_rules(results)

        wb = load_workbook(r'./template.xlsx')
        ws = wb.active

        for data in datas:
            for item in data.items():
                # {'D5': '张宽', 'T5': 25, 'U5': 375, 'V5': 25, 'W5': 217.39, 'X5': 7, 'Y5': 23, 'Z5': 23}
                ws[item[0]] = item[1]

        wb.save(r'./static/考勤结果.xlsx')
        # print('处理完毕')

    @staticmethod
    def __get_results_by_rules(results: list) -> list:
        """
        根据考勤规则 计算个人的结果
        :param result:
        :return:
        """
        datas = []
        for row, result in enumerate(results, start=5):
            jb_cb_count = 0
            jb_jb_count = 0
            # 备注信息
            beizhus = []

            # 工作日加班  餐补+1
            jzr_jbs = result['工作日加班']
            if jzr_jbs:
                for jzr_jb in jzr_jbs:
                    gp = re.search(r'\s(\d+(\.\d+)?)小时', jzr_jb)
                    if gp:
                        if float(gp.group(1)) > 2.0:
                            # 有效加班
                            jb_cb_count += 1

            # 公休日加班 餐补+1 交补+1
            jr_jbs = result['假日加班']
            if jr_jbs:
                for jr_jb in jr_jbs:
                    gp = re.search(r'\s(\d+(\.\d+)?)小时', jr_jb)
                    if gp:
                        if float(gp.group(1)) > 2.0:
                            # 有效加班
                            jb_cb_count += 1
                            jb_jb_count += 1

            # 提取入职信息
            if result['入职信息'][0]:
                beizhu = '入职：' + result['入职信息'][2]
                beizhus.append(beizhu)

            # 提取缺卡信息
            temps = []
            if result['缺卡']:
                for qk in result['缺卡']:
                    temps.append(qk.split(' ')[0][3:])
                beizhus.append('缺卡：' + ' '.join(temps))
            # 提取补卡信息
            if result['补卡']:
                for bk in result['补卡']:
                    temps.append(bk.split(' ')[0][3:])
                beizhus.append('补卡：' + ' '.join(temps))
            # 写结果到模版文件
            data = {
                f'D{row}': result['姓名'],
                f'T{row}': result['实际出勤天数'] + jb_cb_count,
                f'U{row}': round((result['实际出勤天数'] + jb_cb_count) * 15, 2),
                f'V{row}': result['实际出勤天数'] + jb_jb_count,
                f'W{row}': round((result['实际出勤天数'] + jb_jb_count) * 200 / 23, 2),
                f'X{row}': result['公休天数'],
                f'Y{row}': result['应该出勤天数'],
                f'Z{row}': result['实际出勤天数'],
                f'AA{row}': ' '.join(beizhus)
            }
            datas.append(data)
        return datas


if __name__ == '__main__':
    main()
