import logging
import logging.handlers   #需要导入这个
import os
from common import get_path
from conf.conf1 import ConFig
config = ConFig()
#封装的时候，不需要必须使(用类 也可以直接使用函数
def get_logger(logger_name):
    logger = logging.getLogger(logger_name)
    set_level = config.get_conf('log','ste_level')
    logger.setLevel(set_level)    #日志收集级别
    fmt = "%(asctime)s - %(name)s  - %(levelname)s - %(pathname)s -%(message)s "  #日志输出格式
    formate  = logging.Formatter(fmt)       #日志输出格式
    file_name = os.path.join(get_path.log_path,'case.log') #使用绝对地址,最好是使用os.path ，可以确保所有的日志在同一个文件里
    print( file_name)
    file_handler  = logging.handlers.RotatingFileHandler( file_name,maxBytes = 20*1024*1024,backupCount=10,encoding='utf-8')  #文件输出渠道
    out_level =  config.get_conf('log','out_level')                               #RotatingFileHandler 可以定义最大的日志字节
    file_handler.setLevel(out_level)    #日志输出等级
    file_handler.setFormatter(formate)  #日志输出格式
    logger.addHandler(file_handler)      #

    #以下是输出到控制台
    console_handler = logging.StreamHandler()
    console_level = config.get_conf('log','console_level')
    console_handler.setLevel(console_level)
    console_handler.setFormatter(formate)
    logger.addHandler(console_handler)
    return logger
if __name__ == '__main__':

 logger = get_logger(logger_name = 'kkk').error('kkk')
#logger.info('jjjj')


#日志级别设计到配置文件里
#文件路径使用绝对路径
#输出到控制台，定义输出级别为DEBUG
