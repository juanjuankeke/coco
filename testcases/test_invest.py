from common.do_excel import doexcel
from common import get_path
from conf.conf1 import ConFig
import unittest
from ddt import ddt, data
from common.request import request
cases = doexcel(get_path.cases_path).read_data('invest')
from common.test_re import context_1
#from common import test_re    #不需要再次导入
from common.mysql import domysql

ConFig = ConFig()
import json
@ddt
class investTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.t = request()  # 实例化对象 这步很重要，可以确保session运行在同一个对象内
        cls.domysql = domysql()
        #cls.sql = ConFig.get_conf('sql', 'sql_2')
        #domysql.do_sql(cls.sql)

    def setUp(self):
        print('.............开始执行测试用例...............')



    def tearDown(self):
        print('.............测试用例执行结束...............')
    @data(*cases)
    def test_invest(self, case):
        #查找参数化的测试数据
        print('正则之前的数据',case.param)
        print(case.url)
        print(type(case.param))
        params = context_1().replace_1(case.param)
        params = json.loads(params)        #这里需要转成字典
        res = self.t.requests(case.method,case.url,params)
        print(res.text)
        print('正则之后的数据', params)
        print(type(params))
        try:
            self.assertEqual(case.Expected, res.text)
            testresult = 'pass'
            #判断是否加标成功，如果成功就按照借款人的id去数据库查询最新标的记录
            if res.json()['msg'] == '加标成功':
                #admin_id = 1114926  #getattr(context_1,'admin_id ')
                #sql = "select id FROM future.loan where MemberID = '{0}'/ORDER BY CreateTime DESC LIMIT 1".format(admin_id)
                sql = "select id FROM future.loan where MemberID = 1114926 ORDER BY CreateTime DESC LIMIT 1"
                loanId = self.domysql.do_sql(sql)[0]
                setattr(context_1,'loanId',str(loanId))   #这里的loanId，需要转化成str,因为正则处理的是字符串
                #print('嘿嘿嘿嘿嘿嘿',loanId)
        except AssertionError as e:
            testresult = 'faild'
        finally:
            doexcel(get_path.cases_path).write_back('invest', case.case_id + 1, res.text, testresult)
    @classmethod
    def tearDownClass(cls):
        cls.t.session.close()  # 关闭session请求   老师，我之前没有关闭session请求，也，没有报错
        cls.domysql.close()    #关闭数据库
