# _*_ coding:utf-8 _*_
# DATE 2021/8/31
import allure
import pytest

from base.base_unil import BaseUnit
from common.excel_control import ExcelUtil
from common.excel_util import ExcelOperator
from common.logger import log_info,log_error
from pageobjects.testpage.login_page import LoginPage


@allure.epic("web自动化测试")
class TestLogin(BaseUnit):

    # 测试用例登录
    @allure.story("登录流程测试")
    @pytest.mark.parametrize('caseinfo', ExcelUtil().read_excel("/testdatas/web/demo/login_data.xls","登录流程"))
    def test_login(self,caseinfo):
        allure.dynamic.title(caseinfo["用例名称"])
        allure.dynamic.description(caseinfo["数据说明(备注)"])
        loginpage = LoginPage(self.driver)
        log_info(f'执行:{caseinfo["用例名称"]}用例开始')
        loginpage.login(caseinfo["用户名"],caseinfo["用户密码"],caseinfo["断言"])
        log_info(f'执行{caseinfo["用例名称"]}用例结束')

    #
    # @allure.story("登录流程测试1")
    # @pytest.mark.parametrize('caseinfo', ExcelOperator("logincase.xlsx").get_executecase_testdata())
    # def test_cases(self,caseinfo):
    #     self.wb = ExcelOperator("logincase.xlsx")
    #     casedata = caseinfo["casestepdata"]
    #     casename = caseinfo["casename"]
    #     # assertvalue = caseinfo["assert"]
    #     allure.dynamic.title(casename)
    #     log_info(f'执行:{casename}用例开始')
    #     # 记录测试结果
    #     result = True
    #     for index,values in enumerate(casedata):
    #         #执行相应的操作步骤
    #         try:
    #             keyword=values[0]
    #             data=values[1:]
    #             self.Basepage.run(values[0],*data)
    #             # 写入测试结果
    #             self.wb.write_test_result(sheet_name=casename,row=index+2,result="PASS")
    #         except Exception as error:
    #             self.wb.write_test_result(casename,index+2,result="FALSE")
    #             self.sava_page_shot("run")
    #             result = False
    #     # self.asserTrue(result)
    #     assert result == True

