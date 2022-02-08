# encoding:utf-8
# @CreateTime: 2022/1/26 9:57
# @Author: Xuguangchun
# @FlieName: connect_mysql.py
# @SoftWare: PyCharm


import pymysql
from pymysql.cursors import DictCursor


class pymysqltest:

    def __init__(self):  # cursorclass=DictCursor 显示为字典
        # 连接数据库
        self.db = pymysql.connect(
            user='xuguangchun',
            password='test123456',
            host='localhost',
            port=3306,
            database='newsinfomation',
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

    def updateAndDelete(self, sql, values):
        try:
            # 使用execute 执行sql语句
            self.cursor.execute(sql, values)
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
    db1 = pymysqltest()

    # 注: utf-8 ==> utf8
    res = db1.query('select * from news', one=False)
    print(res)

'''
class OperationMysql:
    def __init__(self):
        self.conn = pymysql.connect(
            user='xuguangchun',
            password='test123456',
            host='localhost',
            port=3306,
            database='newsinfomation',
            cursorclass=pymysql.cursors.DictCursor
        )  # 查询以字典返回
        self.cursor = self.conn.cursor()  # 初始化游标对象

    def find_db(self, mysql):
        self.cursor.execute(mysql)
        result = self.cursor.fetchall()
        print(result)
        return result

    def insert_db(self, mysql, values):
        try:
            self.cursor.execute(mysql, values)
            self.conn.commit()
        except:
            self.conn.rollback()
        self.conn.close()
        self.cursor.close()

    def delete_db(self, mysql):
        try:
            self.cursor.execute(mysql)
            self.conn.commit()
        except:
            self.conn.rollback()    # 错误回滚
        self.conn.close()
        self.cursor.close()

# if __name__ == '__main__':
#     connect = OperationMysql()
#     sql2 = 'select title from news'
#
#     connect.find_db(mysql=sql2)
#
#     sql = 'insert into news(title, fu_title) values(%s, %s)'

#     title = 'My name is '
#     fu_title = 'XUGUANCGHUN1'
#     values = (title, fu_title)
#     connect.insert_db(mysql=sql, values=values)
'''