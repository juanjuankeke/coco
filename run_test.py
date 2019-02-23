import unittest
import HTMLTestRunnerNew
from common import get_path
import os

#自动查找testcases目录下，以test开头的.py文件里面的测试类
discover = unittest.defaultTestLoader.discover(start_dir=get_path.testcases_dir,pattern='test_*.py', top_level_dir=None)
#file_name = os.path.join(get_path.resport_dir,'resport.html')
with open(get_path.resport_dir,'wb+') as file:     #等有时间百度查看open函数里的w,wb,b的区别
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                              verbosity=2,
                                              title='python13期的第一份报告',
                                              description='前程贷测试',
                                              tester='娟娟')
    runner.run(discover)         #执行查找到的用例