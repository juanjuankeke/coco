from common.request import request
from common.do_excel import doexcel
import unittest
from ddt import ddt, data
from common import get_path
import json

t = request()
cases = doexcel(get_path.cases_path).read_data('register')  # 获取Excel数据
from conf.conf1 import ConFig
from libext.ddtnew import ddt,data

cof = ConFig().get_conf('sql', 'sql_1')  # 获取SQL语句
from common.mysql import domysql
from log.mylog import get_logger
logger = get_logger(logger_name = 'python')

@ddt
class register(unittest.TestCase):
    def setUp(self):
        self.sql_result = int(domysql().do_sql(cof)[0])  # 把SQL语句发到setup语句下，就可以替换接下来的手机号 setup是执行一次测试用例，就执行一次
        logger.info('..........开始测试............')

    def tearDown(self):
        logger.info('..........测试结束............')

    @data(*cases)
    def test_register(self, cases):
        params = json.loads(cases.param)
        if params["mobilephone"] == "{}phone":  # 判断字典里的手机号是否是"{}phone"
            params["mobilephone"] = self.sql_result + 1  # 重新赋值      #老师 我Excel表里最后三条用例，为什么不通过的 应该是pass才对的 问题已解决 把SQL语句放在setup后
        resp = t.requests(cases.method, cases.url, params)
        try:
            self.assertEqual(cases.Expected, resp.text)
            testresult = 'pass'
            logger.info('第{}条测试用例通过'.format(cases.case_id))
        except AssertionError as e:
            testresult = 'faild'
            logger.error('第{}条测试用例失败'.format(cases.case_id))
        finally:
            doexcel(get_path.cases_path).write_back('register', cases.case_id + 1, resp.text, testresult)
