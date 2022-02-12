#encoding:utf-8
#@CreateTime: 2022/2/8 15:37
#@Author: Xuguangchun
#@FlieName: userModule_v3.py
#@SoftWare: PyCharm

from flask import Flask
from flask import url_for
from flask import request, redirect, jsonify, session
from common.generate_userToken import *
from common.connect_mysql import *
from common.generate_inviteCode import *
from task.invite_task import invite_register
from common.task_getCoins import task_getCoins
"""
session机制 验证会话是否退出 
+
生成用户 token 验证是否已经过期
# app.config['PERMANENT_SESSION_LIFETIME'] = 300 #session 过期时间
# 之前以用户名称作为唯一生成token,后需要修改昵称功能将会导致每次修改都需要重新登录
任务完成后拿去新手任务更新用户金币

"""


class UserModule:
    # currentTime = time.time()
    def verify_session(self, userName):
        if 'username' in session and session.get('username') == userName:
            return True
        else:
            return False

    def verify_token(self, userId):
        if certify_token(userId, request.headers.get('token')) == True:
            return True
        else:
            return False

    def get_inviterName(self, inviteCode):
        sql = "select username from tf_user where invite_code = '%s'" % inviteCode
        mysql = pymysqltest(database='testflask')
        inviterName = mysql.query(sql=sql).get('username')
        return inviterName





app = Flask(__name__)
app.secret_key = 'dhsihdishdisbb8dsjdnjn'
mysql = pymysqltest(database='testflask')


@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    gender = data.get('gender')
    birthday = data.get('birthday')
    create_time = data.get('create_time')
    invite_code = get_inviteCode(5)
    # friendsInvite_code = data.get('invite_code')
    # print(data)
    check_username = "select * from tf_user where username='%s'" % username
    if not all([username, password, gender, birthday, create_time]):
        return jsonify(code=40001, msg='注册失败，缺少参数，请检查')

    if len(mysql.query(sql=check_username, one=False)) != 0:
        return jsonify(code=40002, msg='%s 该用户名已被注册，请重新输入新的用户名！' % username)
    else:
        insert_sql ="insert into tf_user(username, password, gender, birthday, create_time, invite_code) values(%s, %s, %s, %s, %s, %s)"
        values = (username, password, gender, birthday, create_time, invite_code)
        mysql.insert(sql=insert_sql, values=values)

        if invite_register(username=username) == True:  # 若调用结果是True, return 会是一个tuple,否则就是False
            inviterCode = data.get('invite_code')
            inviterName = UserModule().get_inviterName(inviteCode=inviterCode)
            task_getCoins(inviterName=inviterName, taskType=1)

        # if invite_register(username = username) == True:
        #     task_getCoins(inviterName=username, taskType=1)
            return jsonify(code=0, msg='注册成功')
        else:
            return jsonify(code=0, msg='注册成功')


@app.route('/login', methods=['POST'])
def login():
    global token
    global username
    global userId
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    last_login_time = request.headers.get('last_login_time')
    last_login_ip = request.headers.get('last_login_ip')
    update_sql = "update tf_user set last_login_time='%s', last_login_ip='%s' where username ='%s'" % (last_login_time, last_login_ip, username)
    check_username = "select username,password from tf_user where username='%s'" % username
    get_userId = "select id from tf_user where username='%s'" % username
    print(request.headers)
    print(data, type(data))

    if not all([username, password]):
        return jsonify(msg='缺少参数，请检查')
    else:
        check = mysql.query(sql=check_username, one=False)
        userId = str((mysql.query(sql=get_userId)).get('id'))
        if len(check) < 1:
            return jsonify(code=40003, msg='该用户未注册，请先注册再来登录！')
        if len(check) >= 2:
            return jsonify(code=40004, msg='用户数据异常，联系开发者')
        if username == check[0]['username'] and password == check[0]['password']:

            token = generate_token(userId)
            session['username'] = username
            mysql.updateAndDelete(sql=update_sql)
            print(update_sql)

            return jsonify(code=0, msg='登录成功', token=token)
            # return redirect(url_for('login'))
        else:
            return jsonify(code=40005, msg='登录账号密码错误')


@app.route('/logout', methods=['GET'])
def logout():
    session.clear()
    return jsonify(code=0, msg='成功退出登录')
    return redirect(url_for('login'))


@app.route('/userInfo', methods=['GET'])
def userInfo():
    check_userInfo = "select * from tf_user where username='%s'" % username
    print("我是用户id", userId, type(userId))
    if UserModule().verify_session(userName = username) == True:
        pass
    else:
        return jsonify(code=40006, msg='session已过期，请先登录')

    if UserModule().verify_token(userId = userId) == True:

        data = mysql.query(sql=check_userInfo, one=True)
        return jsonify(code=0, msg='成功获取用户信息', data=data)
    else:
        return jsonify(code=40007, msg='token验证失败，请重新登录')

    """
        if 'username' in session and session.get('username') == username:
        pass
    else:
        return jsonify(code=40006, msg='session已过期，请先登录')
    if certify_token(username, request.headers.get('token')) == True:
        check_userInfo = "select * from tf_user where username='%s'" % username
        data = mysql.query(sql=check_userInfo, one=True)
        return jsonify(code=0, msg='成功获取用户信息', data=data)
    else:
        return jsonify(code=40007, msg='token验证失败，请重新登录')
    
    :return: 
    """


@app.route('/inviteFriend', methods=['POST'])
def inviteFriend():
    osUuid = request.headers.get('os_uuid')
    if UserModule().verify_session(userName = username) == True:
        pass
    else:
        return jsonify(code=40006, msg='session已过期，请先登录')

    if UserModule().verify_token(userId = userId) == True:
        pass
    else:
        return jsonify(code=40007, msg='token验证失败，请重新登录')

    if invite_register(username=username) == True:   # 若调用结果是True, return 会是一个tuple,否则就是False
        result = request.get_json()
        inviterCode = result.get('invite_code')
        inviterName = UserModule().get_inviterName(inviteCode=inviterCode)
        task_getCoins(inviterName=inviterName, taskType=1)
        return jsonify(code=0, msg='邀请成功')
    else:
        return jsonify(code=40010, msg='id：%s->设备号：%s 邀请失败，您未能满足邀请成功必备条件！' % (userId, osUuid))

    # inviteCode = data.get('invite_code')


if __name__ == '__main__':

    app.run(host='0.0.0.0', port=1524)
