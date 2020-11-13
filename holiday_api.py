# -*- coding:utf-8 -*-
import json

import requests


def get_holiday():
    """ 获取所有节假日 """
    holidays = []
    year = ['2020']
    month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    day = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
           '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
           '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
    for y in year:
        for m in month:
            for d in day:
                check_date = y + m + d

                res = requests.get(url=f'http://www.easybots.cn/api/holiday.php?d={check_date}').json()
                print(res)
                if res[check_date] != '0':
                    holidays.append(check_date)

    with open('./holidays.json', 'w') as f:
        f.write(json.dumps(holidays))
    print('已经获取到了全年假日')


if __name__ == '__main__':
    get_holiday()
