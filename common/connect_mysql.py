# encoding:utf-8
# @CreateTime: 2022/2/8 15:54
# @Author: Xuguangchun
# @FlieName: connect_mysql.py
# @SoftWare: PyCharm

import pymysql
from pymysql.cursors import DictCursor

"""
# cursorclass=DictCursor 显示为字典
"""


class pymysqltest:

    def __init__(self, database):
        # 连接数据库
        self.db = pymysql.connect(
            user='xuguangchun',
            password='test123456',
            host='localhost',
            port=3306,
            database=database,
            cursorclass=pymysql.cursors.DictCursor)
        # 创建游标对象cursor
        self.cursor = self.db.cursor()

    def query(self, sql, one=True):
        # 使用execute 执行sql语句
        self.cursor.execute(sql)
        if one:
            # 如果为one ，使用 fetchone() 方法获取单条数据
            return self.cursor.fetchone()
        else:
            # 使用 fetchall() 方法获取所有数据
            return self.cursor.fetchall()

    def insert(self, sql, values):
        try:
            # 使用execute 执行sql语句
            self.cursor.execute(sql, values)
            # 提交到数据库执行
            self.db.commit()
        except:
            # 如果发生错误回滚数据
            self.db.rollback()

    def updateAndDelete(self, sql):
        try:
            # 使用execute 执行sql语句
            self.cursor.execute(sql)
            # 提交到数据库执行
            self.db.commit()
        except:
            # 如果发生错误回滚数据
            self.db.rollback()

    def close(self):
        # 关闭游标
        self.cursor.close()
        # 关闭数据库
        self.db.close()


if __name__ == '__main__':
    db1 = pymysqltest(database='testflask')
    res = db1.query(sql="select id from tf_user where invite_code = 'PREX52'")
    print(res)
    # username = '张三'
    # db1.updateAndDelete(sql="insert into tf_user(last_login_time, last_login_ip) values(%s, %s) where username ='%s'"%(11111, 2222, username))
    # 注: utf-8 ==> utf8
    # res = db1.query("select username,password from tf_user where username='张三'", one=False)
    import json

    # print(res)
    # print(res[0])
    # print(res[0]['username'])
    # print(res[0]['password'])
#
