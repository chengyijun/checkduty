# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: upload_demo.py
@time: 2020/11/12 12:28
@desc:
"""
import json
import os

from flask import Flask, request, jsonify
from flask_cors import CORS

from rules import Rule
from test5 import Duty

app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route('/upload', methods=['POST'])
def upload():
    # 保存是长传的excel文件
    uploaded_file = request.files['file']
    # filename = uploaded_file.filename
    filename = '1.xlsx'
    uploaded_file.save(os.path.join('./datas/', filename))

    # 返回api结果
    data = {
        'code': 1,
        'info': '文件上传成功'
    }
    return jsonify(data)


@app.route('/result')
def result():
    # 清洗数据
    duty = Duty()
    datas = duty.get_duty_datas()
    # pprint(datas)
    with open('./datas/results.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(datas, ensure_ascii=False))
    print('执行完毕')
    # 执行规则
    Rule()

    # 返回api结果
    data = {
        'code': 1,
        'info': './datas/考勤结果.xlsx'
    }
    return jsonify(data)


if __name__ == '__main__':
    app.run()
