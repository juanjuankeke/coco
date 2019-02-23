from common.do_excel import doexcel
from common.request import request
from common import get_path
import json
t=request()
cases=doexcel(get_path.cases_path).read_data('login')
import unittest
from ddt import ddt,data
@ddt
class login(unittest.TestCase):
    def setUp(self):
        print('........开始测试.........')
        print('执行第{}条用例'.format(cases))
    @data(*cases)
    def test_login(self,cases):
        data=json.loads(cases.param)
        resp=t.requests(cases.method,cases.url,data)
        try:
            self.assertEqual(resp.text,cases.Expected)
            result='pass'
        except AssertionError as e:
            result = 'faild'
            raise e
        finally:
            doexcel(get_path.cases_path).write_back('login',cases.case_id+1,resp.text,result)
    def tearDown(self):
            print('........测试结束.........')


