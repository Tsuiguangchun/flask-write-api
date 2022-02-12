# encoding:utf-8
# @CreateTime: 2022/2/11 17:04
# @Author: Xuguangchun
# @FlieName: task_getCoins.py
# @SoftWare: PyCharm
from common.connect_mysql import *
import random
"""
1、如果是邀请成功，传入邀请者的名称（给邀请者奖励）
2、传入任务类型
3、其他任务传入用户本人名称

"""


def task_getCoins(inviterName, taskType):
    mysql = pymysqltest(database='testflask')
    get_coin = "select task_coin,coin_percent from tf_task_set where task_type='%s'" % taskType
    get_balance = "select balance from tf_user where username='%s'" % inviterName
    result = mysql.query(sql=get_coin)
    task_coin = result.get('task_coin')
    coin_percent = result.get('coin_percent')
    balance = mysql.query(sql=get_balance).get('balance')
    print(balance)
    if coin_percent != 0:
        coins = task_coin + (task_coin * random.randrange(0, coin_percent, 1)/100)
        update_coins = balance+coins
        update_balance = "update tf_user set balance=%s where username='%s'" % (update_coins, inviterName)
        mysql.updateAndDelete(sql=update_balance)
        print(coins)
        return coins

    else:
        coins = task_coin
        update_coins = balance + coins
        update_balance = "update tf_user set balance=%s where username='%s'" % (update_coins, inviterName)
        mysql.updateAndDelete(sql=update_balance)
        return coins

