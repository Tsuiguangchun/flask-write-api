#encoding:utf-8
#@CreateTime: 2022/2/10 10:46
#@Author: Xuguangchun
#@FlieName: invite_task.py
#@SoftWare: PyCharm
from flask import request,jsonify
from common.connect_mysql import *
import time
"""
如果邀请码不为空，去查询该设备或者用户id是否已经邀请记录过，没有记录就写入邀请记录表，判断如果
如果邀请码为空，或者邀请码不存在，正常注册成功
只记录成功用户
"""


def invite_register(username):

    data = request.get_json()
    inviteCode = data.get('invite_code')
    username = username
    osUuid = request.headers.get('os_uuid')
    mysql = pymysqltest('testflask')
    invite_success_time = int(time.time())

    if inviteCode is not None:
        sql = "select os_uuid from invite_record where os_uuid = '%s'" % osUuid
        sql2 = "select id,username from tf_user where invite_code = '%s'" % inviteCode
        sql3 = "select id from tf_user where username = '%s'" % username
        sql4 = "insert into invite_record(username, user_id, invite_user_id, invite_code, os_uuid, invite_success_time) values(%s, %s, %s, %s, %s, %s)"

        check_osUuid = mysql.query(sql=sql, one=False)
        invite_code_info = mysql.query(sql=sql2)
        # print('邀请者id和名称',invite_code_info)

        user_id = (mysql.query(sql=sql3)).get('id')
        os_uuid = osUuid
        sql5 = "select user_id from invite_record where user_id = '%s'" % user_id
        check_inviteRecord_userId = mysql.query(sql=sql5, one=False)

        # print("用户是否在邀请记录表里面", check_inviteRecord_userId)
        # print(value)
        # print("邀请用户id",invite_user_id)
        # print("设备id", check_osUuid)
        if invite_code_info is not None:
            pass
        else:
            return False
        if len(check_osUuid) > 0 or len(check_inviteRecord_userId) > 0:
            # return jsonify(code=40009, msg='%s 此设备已被邀请')
            return False
        else:
            invite_user_id = invite_code_info.get('id')
            value = (username, user_id, invite_user_id, inviteCode, os_uuid, invite_success_time)
            mysql.insert(sql=sql4, values=value)
            # inviterName = invite_code_info.get('username')
            # print("邀请函数打印邀请者id：", inviterName)
            return True
