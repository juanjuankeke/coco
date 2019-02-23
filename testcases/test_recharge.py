import unittest
from ddt import ddt, data
from common.do_excel import doexcel
from common.request import request
from common import get_path
import json

cases = doexcel(get_path.cases_path).read_data('recharge')


# 老师我之前没有把数据和实例化对象都放在类外面，为什么也可以执行成功的
@ddt
class rechrge(unittest.TestCase):
    # cases = doexcel(get_path.cases_path).read_data('recharge')
    @classmethod  # 类方法
    def setUpClass(cls):  # 针对整个测试类执行的    整个类执行一次
        cls.t = request()  # 实例化对象 这步很重要，可以确保session运行在同一个对象内

    def setUp(self):  # 针对测试方法执行的  每个测试用例执行一次
        print('.........开始执行测试用例...........')

    def tearDown(self):
        print('.........测试用例执行结束...........')

    @data(*cases)
    def test_rechrge(self, cases):
        print('开始执行第{}条用例'.format(cases.case_id))
        data = json.loads(cases.param)
        res = self.t.requests(cases.method, cases.url, data)  # 这里使用self调用
        text = json.loads(res.text)
        try:
            self.assertEqual(int(text['code']), (cases.Expected))
            tesrresult = 'pass'
        except AssertionError as e:
            tesrresult = 'faild'
            raise e
        finally:
            doexcel(get_path.cases_path).write_back('recharge', cases.case_id + 1, res.text, tesrresult)

    @classmethod  # 类方法
    def tearDownClass(cls):
        cls.t.session.close()  # 关闭session请求   老师，我之前没有关闭session请求，也，没有报错
