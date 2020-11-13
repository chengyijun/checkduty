# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: read_excel.py
@time: 2020/11/11 10:01
@desc:
"""
import xlrd


def main():
    template = xlrd.open_workbook('./template.xlsx')
    sheet = template.sheet_by_index(0)
    print(sheet.nrows, sheet.ncols)
    
    sheet.write(8, 20, 'test')


if __name__ == '__main__':
    main()
