# _*_ coding:utf-8 _*_
# DATE 2021/8/31
import time
from base.base_operation import BasePage
from common.excel_util import ExcelOperator
from common.logger import log_info, log_error
from selenium import webdriver
from config import config


class BaseUnit:

    def setup_class(cls):
        pass

    # 测试用例执行前的准备工作
    def setup_method(self):
        try:
            timestr = time.strftime("%Y/%m/%d %H:%M:%S", time.localtime())
            browser = config.browsertype
            self.driver = getattr(webdriver,browser)()
            self.Basepage = BasePage(self.driver)
            log_info(f"-----------WEB自动化测试开始-----------")
            log_info(f"用例执行时间：{timestr}")
            log_info(f"打开{browser}浏览器")
            self.driver.maximize_window()
            # 智能等待
            self.driver.implicitly_wait(10)
        except:
            log_error(f"打开浏览器失败")
        return self.driver


    #测试用例执行后的扫尾工作
    def teardown_method(self):
        log_info("----------测试用例执行结束----------\n\n\n\n")
        time.sleep(3)
        self.driver.quit()

    @classmethod
    def teardown_class(cls):
        ExcelOperator("logincase.xlsx").write_cases_result()

