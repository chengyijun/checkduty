# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: wirte_excel.py
@time: 2020/11/11 9:58
@desc:
"""


def main():
    import xlwt
    # 创建一个workbook 设置编码
    workbook = xlwt.Workbook(encoding='utf-8')
    # 创建一个worksheet
    worksheet = workbook.add_sheet('My Worksheet')
    
    # 写入excel
    # 参数对应 行, 列, 值
    worksheet.write(1, 0, label='this is test')

    # 保存
    workbook.save('Excel_test.xls')


if __name__ == '__main__':
    main()
