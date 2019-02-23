import os

path = os.path.abspath(__file__)  # 获取当前文件的绝对路径
path_1 = os.path.dirname(os.path.dirname(path))  # 获取当前文件绝对路径的上上级路径
cases_path = os.path.join(path_1, 'datas')
cases_path = os.path.join(cases_path, 'cases.xlsx')  # 获取测试用例的地址
config_path = os.path.join(path_1, 'conf')
config_path = os.path.join(config_path, 'configparser')  # 建议最好是一步一步的填写地址，path_1,'conf','configparser'分开写
config1_path = os.path.join(path_1, 'conf')
config1_path = os.path.join(config1_path, 'configparser1')
globle_path = os.path.join(path_1, 'conf')
globle_path = os.path.join(globle_path, 'globle')
log_path = os.path.join(path_1, 'log')
testcases_dir = os.path.join(path_1, 'testcases')       #测试类地址
resport_dir = os.path.join(path_1, 'resport')           #报告地址
resport_dir = os.path.join(resport_dir, 'resport.html')


if __name__ == '__main__':
    print(resport_dir)
