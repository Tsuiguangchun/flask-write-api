#encoding:utf-8
#@CreateTime: 2022/2/9 17:23
#@Author: Xuguangchun
#@FlieName: generate_inviteCode.py
#@SoftWare: PyCharm
import random


def get_inviteCode(count):
    seed = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    sa = []
    for i in range(count):
        sa.append(random.choice(seed))
    inviteCode = ''.join(sa).upper()
    # print('邀请码', inviteCode)
    return inviteCode

