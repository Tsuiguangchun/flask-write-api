# encoding:utf-8
# @CreateTime: 2022/1/29 10:27
# @Author: Xuguangchun
# @FlieName: learn_flask01.py
# @SoftWare: PyCharm
import json
from flask import Flask
from flask import url_for
from flask import request, redirect, jsonify, session
from common.generate_userToken import *
import time
import base64
import hmac
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
"""
使用session 机制 鉴定会话是否有效 
"""
app = Flask(__name__)
app.secret_key = 'dhsihdishdisbb8dsjdnjn'
app.config['PERMANENT_SESSION_LIFETIME'] = 300


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')


    print(request.headers)
    print(data, type(data))

    if request.method == 'POST':
        if not all([username, password]):
            return jsonify(msg='缺少参数，请检查')
        else:
            if username == 'xuguangchun' and password == 'xuguangchun123':
                token = generate_token(username)
                session['username'] = username
                return jsonify(msg='登录成功', token=token)
                return redirect(url_for('login'))
            else:
                return jsonify(msg='登录账号密码错误')
    else:
        return jsonify(msg='注意请求方法')


@app.route('/logout', methods=['GET'])
def logout():
    session.clear()
    return jsonify(msg='退出登录')
    return redirect(url_for('login'))


@app.route('/userInfo', methods=['GET'])
def userInfo():
    if 'username' in session and session['username'] == 'xuguangchun':
        return jsonify(data={'userId': 12, 'username': '徐光春', 'age': 26}, msg='获取用户%s信息' % session['username'])
    else:
        return jsonify(msg='session已过期，请先登录')


app.run(host='0.0.0.0', port=1524)
