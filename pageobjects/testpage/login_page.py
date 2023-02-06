# _*_ coding:utf-8 _*_
# DATE 2021/8/31
import time
from base.base_operation import BasePage
from config.config import base_url


class LoginPage(BasePage):

    """
    实现用例的方法，需要继承BasePage，调用BasePage中基础操作来实现登录
    """
    login_url = base_url+"cognition/"

    el_pwdlogin = ["xpath", "//*[@id='loginForm']/div[2]/div/input[2]"]
    # 输入密码
    el_passwd = ["xpath", "//*[@id='loginForm']/div[3]/div/input[2]"]
    # 点击登录
    el_loginbutten = ["xpath", "//*[@id='submitBtn']"]
    # 断言
    el_assertTextIn = ["xpath", "//*[@id='searchForm']/div[4]/button[1]"]



    def login(self,usname,passwd,el_assert):
        # 实现登录的步骤
        self.open_url(self.login_url)
        time.sleep(2)
        self.input(self.el_pwdlogin[0],self.el_pwdlogin[1],value=usname,)
        # 输入密码，调用BasePage中的输入方法，元素的定位是通过读取pagelocations.login_page_locs下的配置文件中密码元素
        self.input(self.el_passwd[0],self.el_passwd[1],value=passwd)
        # 点击登录，调用BasePage中的输入方法，元素的定位是通过读取pagelocations.login_page_locs下的配置文件中登录按钮元素
        self.click(self.el_loginbutten[0],self.el_loginbutten[1])
        time.sleep(2)
        self.assertTextIn(self.el_assertTextIn[0],self.el_assertTextIn[1],str=el_assert)

