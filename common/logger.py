# _*_ coding:utf-8 _*_
# DATE 2021/8/26

import logging
import time
from config import dir_config as dir
from config import config


class LoggerUtil:

    def create_log(self,logger_name='log'):
        #创建一个日志对象
        self.logger = logging.getLogger(logger_name)
        # 设置全局的日志级别DEBUG < INFO < WARNING < ERROR < CRITICAL
        self.logger.setLevel(logging.DEBUG)
        #防止日志重复
        if not self.logger.handlers:
            #----------文件日志------------
            # 获得日志文件的名称
            # 日志的名称名称组成是有get_object_path项目根路径+日志文件存储的路径'/logs/'+日志的名称（通过read_config方法读取）
            # config.yml文件中的log下的log_name的值，+ 当前的时间戳str(int(time.time()))+后缀名".log"
            self.file_log_path = dir.logs_dir +config.log_name +str(int(time.time()))+".log"
            #创建文件日志的控制器
            self.file_handler = logging.FileHandler(self.file_log_path,encoding='utf-8')
            #设置文件日志的级别，日志的级别（通过read_config方法读取） config.yml文件中的log下的log_level的值
            file_log_lever = str(config.log_level).lower()
            # 判断日志的级别生成不同的日志
            if file_log_lever == 'debug':
                self.file_handler.setLevel(logging.DEBUG)
            elif file_log_lever == 'info':
                self.file_handler.setLevel(logging.INFO)
            elif file_log_lever == 'warning':
                self.file_handler.setLevel(logging.WARNING)
            elif file_log_lever == 'error':
                self.file_handler.setLevel(logging.ERROR)
            elif file_log_lever == 'critical':
                self.file_handler.setLevel(logging.CRITICAL)
            # 设置文件日志的格式，日志的格式（通过read_config方法读取） config.yml文件中的log下的log_format的值
            self.file_handler.setFormatter(logging.Formatter(config.log_format))
            # 将控制器加入到日志对象
            self.logger.addHandler(self.file_handler)

            # ----------控制台日志------------
            # 创建控制台日志的控制器
            self.console_handler = logging.StreamHandler()
            # 设置控制台日志的级别
            console_log_lever = str(config.log_level).lower()
            if console_log_lever == 'debug':
                self.console_handler.setLevel(logging.DEBUG)
            elif console_log_lever == 'info':
                self.console_handler.setLevel(logging.INFO)
            elif console_log_lever == 'warning':
                self.console_handler.setLevel(logging.WARNING)
            elif console_log_lever == 'error':
                self.console_handler.setLevel(logging.ERROR)
            elif console_log_lever == 'critical':
                self.console_handler.setLevel(logging.CRITICAL)
            # 设置控制台日志的格式
            self.console_handler.setFormatter(logging.Formatter(config.log_format))
            # 将控制器加入到日志对象
            self.logger.addHandler(self.console_handler)

        return self.logger

# 函数：输出正常日志
def log_info(log_message):
    LoggerUtil().create_log().info(log_message)

# 函数：输出错误日志
def log_error(log_message):
    LoggerUtil().create_log().error(log_message)



if __name__ == '__main__':
    log_info("你好")


