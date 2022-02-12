# encoding:utf-8
# @CreateTime: 2022/2/7 17:11
# @Author: Xuguangchun
# @FlieName: generate_userToken.py
# @SoftWare: PyCharm

import time
import base64
import hmac
from flask import jsonify


# 生成token 入参：用户id
# int类型没有encode属性，需转换str
def generate_token(key, expire=300):
    ts_str = str(time.time() + expire)
    ts_byte = ts_str.encode("utf-8")
    sha1_tshexstr = hmac.new(key.encode("utf-8"), ts_byte, 'sha1').hexdigest()
    token = ts_str + ':' + sha1_tshexstr
    b64_token = base64.urlsafe_b64encode(token.encode("utf-8"))
    return b64_token.decode("utf-8")


# 验证token 入参：用户id 和 token
def certify_token(key, token):
    token_str = base64.urlsafe_b64decode(token).decode('utf-8')
    token_list = token_str.split(':')
    if len(token_list) != 2:
        return jsonify(code=10001, msg='token值错误，请检查参数')
        # return False
    ts_str = token_list[0]
    if float(ts_str) < time.time():
        # token expired
        print(float(ts_str), time.time())
        return jsonify(code=10002, msg='token 过期，请重新登录')
        # return False
    known_sha1_tsstr = token_list[1]
    sha1 = hmac.new(key.encode("utf-8"), ts_str.encode('utf-8'), 'sha1')
    calc_sha1_tsstr = sha1.hexdigest()
    if calc_sha1_tsstr != known_sha1_tsstr:
        # token certification failed
        return jsonify(code=10003, msg='token 验证失败，请联系开发者')
        # return False
    # token certification success
    return True
