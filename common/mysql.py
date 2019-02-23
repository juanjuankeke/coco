import pymysql
import pymysql
from conf.conf1 import ConFig


class domysql:
    def __init__(self):
        self.host = ConFig().get_conf('sql', 'host')
        self.user = ConFig().get_conf('sql', 'user')
        self.password = ConFig().get_conf('sql', 'password')
        self.port = eval(ConFig().get_conf('sql', 'port'))
        self.mysql = pymysql.connect(host=self.host, user=self.user, password=self.password,
                                     port=self.port)  # 这里不传入数据库名，因为真实的项目下，不会就一个数据库的，所以查询语句直接填写对应的数据库名
        self.cursor = self.mysql.cursor()  # 建立游标

    def do_sql(self, sql):
        # 数据库名字也要添加
        cursor = self.mysql.cursor()  # 建立游标
        #sql = ConFig().get_conf('sql', 'sql_2')     #封装的时候，不需要写具体的SQL语句
        cursor.execute(sql)  # 执行SQL语句
        res = cursor.fetchone()  # 返回的是元祖，返回执行的测试语句
        return res

    def close(self):
        self.cursor.close()  # 关闭浮标
        self.mysql.close()  # 关闭数据库


if __name__ == '__main__':
    sql = ConFig().get_conf('sql', 'sql_1')
    domysql().do_sql(sql)[0]
    print(int(domysql().do_sql(sql)[0]))
    domysql().close()
