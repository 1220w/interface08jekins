"""为程序运行添加日志
流程：
  配置
     1.导包
     2.获取日志器对象
     3.设置日志处理器（控制输出目标）
     4.设置格式化器
     5.组织上述对象
  调用
  logging.INFO("--------")
"""
import os
import logging
import logging.handlers
# 封装URL的前缀
import time

BASE_URL = "http://182.92.81.159/api/sys/"
# 动态获取绝对路径
PRO_PATH = os.path.dirname(os.path.abspath(__file__))
TOKEN = None
ID = None


def my_log_config():
    # 获取日志器对象
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    # 设置日志处理器（控制输出目标）
    tol = logging.StreamHandler()  # 默认控制台
    filename = PRO_PATH + "/log/myAuto" + time.strftime()
    to2 = logging.handlers.TimedRotatingFileHandler
