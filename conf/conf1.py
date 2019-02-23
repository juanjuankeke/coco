import configparser
from common import get_path


class ConFig:
    def __init__(self):  # （初始化函数，实例化对象时，会自动执行）
        self.cf = configparser.ConfigParser()  # 实例化
        self.cf.read(get_path.globle_path, encoding='utf-8')  # 定位配置文件
        open = self.cf.getboolean('switch', 'open')
        if open:#布尔值可以直接作为判断条件
            self.cf.read(get_path.config_path, encoding='utf-8')
        else:
            self.cf.read(get_path.config1_path, encoding='utf-8')

    def get_conf(self, section: object, option: object) -> object:
        res = self.cf.get(section, option)  # 根据section和option取值
        return res  # 返回结果


if __name__ == '__main__':
    res = ConFig().get_conf('http', 'url')
    print(res)
    # ctrl+alt+l      一键优化代码       Reformat   code
