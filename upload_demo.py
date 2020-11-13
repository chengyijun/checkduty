# -*- coding:utf-8 -*-
"""
@author: chengyijun
@contact: cyjmmy@foxmail.com
@file: upload_demo.py
@time: 2020/11/12 12:28
@desc:
"""
import os

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route('/test_api', methods=['POST'])
def test_api():
    uploaded_file = request.files['file']
    filename = uploaded_file.filename
    uploaded_file.save(os.path.join('./', filename))
    data = {
        'code': 1,
        'info': f'{filename} 上传成功'
    }
    return jsonify(data)


if __name__ == '__main__':
    app.run()
