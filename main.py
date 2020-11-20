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

from flask import Flask, request, jsonify, Blueprint

from utils import delete_target_dir

# from flask_cors import CORS

api = Blueprint('api', __name__)


@api.route('/upload', methods=['POST'])
def upload():
    delete_target_dir('./datas')
    os.mkdir('./datas')
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


@api.route('/result')
def result():
    delete_target_dir('./static')
    os.mkdir('./static')

    # 清洗数据
    if not os.path.exists('./datas/1.xlsx'):
        data = {
            'code': 0,
            'info': '未上传excel'
        }
        return jsonify(data)
    from clean_data import Duty

    duty = Duty()
    datas = duty.get_duty_datas()
    # pprint(datas)
    with open('./datas/results.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(datas, ensure_ascii=False))

    # 执行规则
    from rules import Rule
    Rule()

    # 返回api结果
    data = {
        'code': 1,
        'info': 'http://192.168.10.129:5000/static/考勤结果.xlsx'
    }
    print('执行完毕')
    return jsonify(data)


app = Flask(__name__)
app.register_blueprint(api, url_prefix='/api')
# CORS(app, supports_credentials=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
