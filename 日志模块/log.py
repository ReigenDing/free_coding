# coding=utf-8
from datetime import datetime
from logging.handlers import RotatingFileHandler

__author__ = 'ReigenDing'
import logging

logging.basicConfig(level=logging.DEBUG,
                    filename='./log/log.log',
                    filemode='w',
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
# use logging
logging.info('this is a loggging info message')
logging.debug('this is a loggging debug message')
logging.warning('this is loggging a warning message')
logging.error('this is an loggging error message')
logging.critical('this is a loggging critical message')


# ===========================================================================#


# 第一步，创建一个logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)  # Log等级总开关

# 第二步，创建一个handler，用于写入日志文件
logfile = './logger.txt'
fh = logging.FileHandler(logfile, mode='w')
fh.setLevel(logging.INFO)  # 输出到file的log等级的开关

# 第三步，再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)  # 输出到console的log等级的开关

# 第四步，再创建一个handler，这个handler可以控制保存日志文件的大小和数量
logfile2 = './log/logger.txt'
fh_ = RotatingFileHandler(logfile2, mode='a', maxBytes=1*1024, backupCount=5, encoding=None, delay=0)
fh_.setLevel(logging.INFO)

# 第五步，定义handler的输出格式
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
fh.setFormatter(formatter)
ch.setFormatter(formatter)
fh_.setFormatter(formatter)

# 第六步，将logger添加到handler里面
logger.addHandler(fh)
logger.addHandler(ch)
logger.addHandler(fh_)


dt = datetime.now()
print('时间：(%Y-%m-%d %H:%M:%S %f): ' , dt.strftime( '%Y-%m-%d %H:%M:%S %f' ))
# 日志
logger.debug('this is a logger debug message')
logger.info('this is a logger info message')
logger.warning('this is a logger warning message')
logger.error('this is a logger error message')
logger.critical('this is a logger critical message')


for i in range(100):
    logger.info('test info')





