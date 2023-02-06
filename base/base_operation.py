# _*_ coding:utf-8 _*_
# DATE 2021/8/30
import os
import time
import win32con
import win32gui
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.dir_config import screen_dir
from common.logger import LoggerUtil as log
from selenium.webdriver.support.ui import Select
from common.mysql_util import MysqlENC

class BasePage:
    """
    BasePage:定义每个页面的相同属性及方法
    """
    def __init__(self,driver):
        self.driver = driver
        self.logger = log().create_log()
        # self.mysql = MysqlENC()

    # 根据关键字可以运行这个类中的所有方法
    def run(self, keyword, *args):
        getattr(self, keyword)(*args)
        self.logger.info(f"执行完关键字{keyword}方法成功")


    # 定位单个元素方法
    def locator(self, by, byvalue, time=10):
        """定位单个元素方法"""
        try:
            self.driver.implicitly_wait(time)
            ele = self.driver.find_element(by, byvalue)
            self.logger.info(f"定位元素{by, byvalue}，定位元素成功！")
            return ele
        except:
            self.sava_page_shot("locator")
            raise self.logger.error(f"无法定位元素{by, byvalue}，定位元素失败！")

    # 定位多个元素方法，返回的是对象列表
    def locators(self, by, byvalue, time=10):
        """定位单个元素方法"""
        try:
            self.driver.implicitly_wait(time)
            ele = self.driver.find_elements(by, byvalue)
            self.logger.info(f"定位元素{by, byvalue}，定位元素成功！")
            return ele
        except:
            self.sava_page_shot("locators")
            raise self.logger.error(f"无法定位元素{by, byvalue}，定位元素失败！")

    # 加载打开一个url地址
    def open_url(self,url):
        """
        加载项目地址
        :param url:项目地址
        """
        try:
            self.driver.get(url)
            self.logger.info(f"加载项目地址：{url}")
        except:
            self.sava_page_shot("open_url")
            raise self.logger.info(f"加载项目地址出错：加载失败")

    # 窗口的常规操作，传参：close/quit/forward/back/refresh/maximize_window/maximize_window
    def window(self, control):
        """
        浏览器操作：关闭当前窗口，关闭浏览器，前进，后退，刷新，窗口最大化，窗口最小化
        :param control:关闭当前窗口 close，关闭浏览器 quit，前进 forward，后退 back，刷新 refresh
        窗口最大化：maximize_window 窗口最小化：maximize_window
        """
        try:
            self.con = getattr(self.driver, control)()
            self.logger.info(f"浏览器{control}操作正常")
        except:
            self.sava_page_shot("window")
            raise self.logger.error(f"浏览器{control}操作失败")


# ----------------------------------------元素常用操控---------------------------------------------------------------

    # 输入内容
    def input(self, by, byvalue,value):
        try:
            self.locator(by, byvalue).send_keys(value)
            self.logger.info(f"操作元素({by},{byvalue})输入{value}成功")
        except:
            self.sava_page_shot("window")
            raise self.logger.error(f"操作元素({by},{byvalue})输入{value}有异常！")

    # 点击元素
    def click(self, by, byvalue):
        """点击元素"""
        try:
            self.locator(by, byvalue).click()
            self.logger.info(f"操作元素({by},{byvalue})点击成功")
        except:
            self.sava_page_shot("click")
            raise self.logger.error(f"操作元素({by},{byvalue})点击失败")

    # 清空内容
    def clear(self, by, byvalue):
        """清空内容"""
        try:
            self.locator(by, byvalue).click()
            self.logger.info(f"操作元素({by},{byvalue})清楚内容成功")
        except:
            self.logger.error(f"操作元素({by},{byvalue})清楚内容失败")
            self.sava_page_shot("clear")

    # 截图功能
    def sava_page_shot(self,img_name):
        """截图功能"""
        try:
            filename=os.path.join(screen_dir,img_name+'.png')
            self.driver.save_screenshot(filename)
            self.logger.info(f"截取当前网页，存储的路径:{filename}，截图成功")
        except:
            self.logger.error(f"截图功能出现错误")

# ----------------------------------------切换---------------------------------------------------------------

    # 切换浏览器句柄/标签
    def switch_handle(self, title):
        """
        句柄切换
        :param title: 切换句柄的页面title的名称
        """
        try:
            for handle in self.driver.window_handles:
                self.driver.switch_to.window(handle)
                if self.driver.title.__contains__(title):
                    break
                self.logger.info(f"切换到句柄{title}成功")
        except:
            self.logger.error(f"切换到句柄{title}出现错误")
            self.sava_page_shot("switch_handle")

    # 切换到指定的iframe 传参 1.id或者name  2.iframe所在元素的定位by和byvalue    3.iframe的索引
    def switch_iframe(self,iframe_name,by=None,byvalue=None,index=0):
        """
        切换到指定的iframe
        :param iframe_value: 1.iframe的id或者name   2.iframe所在元素的定位el    3.iframe的索引
        """
        try:
            el = self.locator(by,byvalue)
            if el:
                self.driver.switch_to.frame(el)(index)
                self.logger.info(f"切换到iframe{iframe_name}成功")
            else:
                self.driver.switch_to.frame(iframe_name)
        except:
            self.logger.error(f"切换到iframe{iframe_name}出现错误")
            self.sava_page_shot("switch_iframe")

    # 切换到上一层iframe
    def switch_parent(self):
        """切换到上一层iframe"""
        try:
            self.driver.switch_to.parent()
            self.logger.info(f"切换到上一层iframe成功")
        except:
            self.logger.info(f"切换到上一层iframe失败")
            self.sava_page_shot("switch_parent")

    # 从iframe切换到主文档
    def default_content(self):
        """从iframe切换到主文档"""
        try:
            self.driver.switch_to.default_content()
            self.logger.info(f"切换到主文档成功")
        except:
            self.logger.info(f"切换到主文档失败")
            self.sava_page_shot("default_content")

# ----------------------------------------断言---------------------------------------------------------------

    # web断言元素文本内容等于某个字符
    def assertText(self,by,byvalue,expect):
        """web断言元素文本内容等于某个字符"""
        fact=self.locator(by,byvalue).text
        if expect!=fact:
            self.logger.error(f"断言元素({by},{byvalue})，assertText：{expect}!={fact},断言失败")
            raise Exception(f"断言失败：{expect}!={fact}")
        self.logger.info(f"断言元素({by},{byvalue})，assertText：{expect}={fact},断言成功")


    # web断言URL是否包含某个字符
    def assertUrlIn(self,str):
        """web断言URL是否包含某个字符"""
        url=self.driver.current_url
        if str not in url:
            self.logger.error(f"断言assertIn,{str} not in {url}")
            raise Exception(f"断言失败：{str} not in {url}")
        self.logger.info(f"断言assertIn：{str}  in {url}，断言成功！")
        self.sava_page_shot(self.driver.title)

    # web断言元素文本内容是否包含某字符串
    def assertTextIn(self,by,byvalue,str):
        """web断言元素文本内容是否包含某字符串"""
        fact=self.locator(by,byvalue).text
        if str not in fact:
            self.logger.error(f"断言assertTextIn,{str} not in {fact}")
            raise Exception(f"断言失败：{str} not in {fact}")
        self.logger.info(f"断言assertTextIn：{str}  in {fact}，断言成功！")


    def assertMysql(self,methon,sql,expected=None):
        """
        数据结构断言验证，成功返回True,失败返回False
        :param methon: 传入方法名称，select/insert/update/delete
        :param sql: 执行sql的语句
        :param expected: 预期的值，只有select使用  expected格式例如{'ENAME': '杨希'}
        :return:
        """
        if methon == "select":
            self.result = self.mysql.select(sql)
            for data in self.result:
                for key in expected:
                    if (key in data) & (data[key] == expected[key]):
                        self.logger.info(f"断言assertMysql：{expected}  in {self.result}，断言成功！")
                    else:
                        raise Exception ("查询断言出现错误")
        elif methon == "insert":
            self.result = self.mysql.insert(sql)
            if self.result == 0:
                raise Exception ("查询断言出现错误")
            else:
                self.logger.info(f"断言assertMysql：成功插入 {self.result}条记录，断言成功！")
        elif methon == "update":
            self.result = self.mysql.update(sql)
            if self.result == 0:
                raise Exception("查询断言出现错误")
            else:
                self.logger.info(f"断言assertMysql：成功修改 {self.result}条记录，断言成功！")

        elif methon == "delete":
            self.result = self.mysql.delete(sql)
            if self.result == 0:
                raise Exception("查询断言出现错误")
            else:
                self.logger.info(f"断言assertMysql：成功删除 {self.result}条记录，断言成功！")



# ----------------------------------------等待---------------------------------------------------------------
    # 强制睡眠等待
    def sleep(self, s):
        """强制睡眠等待"""
        try:
            time.sleep(int(s))
            self.logger.info(f"停留{s}秒")
        except:
            self.logger.error(f"执行停留{s}秒，有异常！")

    # 等待元素存在：传参传元素的定位
    def wait_ele_visibility(self, by, byvalue, timeout=15, poll_fre=0.5):
        """
        等待元素存在
        :param loc: 定位表达式
        :param timeout: 等待时间
        :param poll_fre: 查询间隔
        """
        try:
            loc = (by,byvalue)
            WebDriverWait(self.driver,timeout, poll_fre).until(EC.visibility_of_element_located(loc))
            self.logger.info(f"等待元素{loc}存在成功")
        except:
            self.logger.error(f"等待元素存在出错")
            self.sava_page_shot("wait_ele_visibility")

    # 隐式等待或者智能等待
    def implicitly_wait(self, time):
        """
        隐式等待
        :param time: 等待时长
        """
        try:
            self.driver.implicitly_wait(time)
            self.logger.info(f"隐式等待{time}秒正常")
        except:
            self.logger.error(f"隐式等待{time}秒出错")

    # ----------------------------------------窗口常用操控---------------------------------------------------------------

    # 关闭当前窗口
    def close(self):
        """关闭当前窗口"""
        close = self.driver.close
        return close

    # 关闭浏览器
    def quit(self):
        """关闭浏览器"""
        quit = self.driver.quit
        return quit

    # 窗口前进
    def forward(self):
        """前进窗口"""
        forward = self.driver.forward
        return forward

    # 窗口后退
    def back(self):
        """后退窗口"""
        back = self.driver.back
        return back

    # 刷新当前窗口
    def refresh(self):
        """刷新当前窗口"""
        refresh = self.driver.refresh
        return refresh

    # 窗口最大化
    def maximize_window(self):
        """窗口最大化"""
        maximize_window = self.driver.maximize_window
        return maximize_window

    # 窗口最小化
    def minimize_window(self):
        """窗口最小化"""
        minimize_window = self.driver.minimize_window
        return minimize_window


# ----------------------------------------浏览器窗口的操控和设置---------------------------------------------------------------
    # 打开一个新的窗口
    def open_new_windos(self,url):
        """
        打开一个新的窗口
        :param url:地址
        """
        try:
            js = f'window.open("{url}")'
            self.driver.execute_script(js)
            self.logger.info(f"打开新的窗口成功，并加载了地址：{url}")
        except:
            self.logger.error(f"打开新的窗口失败")
            self.sava_page_shot("open_new_windos")

    # 设置当前窗口的大小
    def setting_windows_size(self, width, height):
        """
        设置当前窗口的大小
        :param width: 宽度
        :param height: 高度
        """
        try:
            self.driver.set_window_size(width, height)
            self.logger.info("设置当前窗口的大小正常")
        except:
            self.logger.error("设置当前窗口的大小出错")

    # 获取当前窗口的大小
    def get_windows_size(self, size):
        """
        获取当前窗口的大小
        :param size: 1.size  获取当前窗口的宽和高
                     2.width 获取当前窗口的宽
                     2.height 获取当前窗口的高
        :return:width/height/width,height
        """
        try:
            win_width = self.driver.get_window_size().get('width')
            win_height = self.driver.get_window_size().get('height')
            if size == "width":
                self.logger.info("获取当前窗口的width")
                return win_width
            elif size == "height":
                self.logger.info("获取当前窗口的height")
                return win_height
            elif size == "size":
                self.logger.info("获取当前窗口的width和height")
                return win_width, win_height
            else:
                self.logger.error("参数输入有错")
        except:
            self.logger.error("获取当前窗口大小出现错误")

    # 获取当前窗口的坐标:1.传参x 获取x的坐标  2.传参y 获取y的坐标 3.传参coordinate 获取x和y的坐标
    def get_windows_coordinate(self, coordinate):
        """
        获取当前窗口的坐标
        :param coordinate:1.传参x 获取x的坐标  2.传参y 获取y的坐标 3.传参coordinate 获取x和y的坐标
        :return:
        """
        try:
            x = self.driver.get_window_position().get('x')
            y = self.driver.get_window_position().get('y')
            if coordinate == "x":
                self.logger.info("获取当前窗口的x坐标")
                return x
            elif coordinate == "y":
                self.logger.info("获取当前窗口的y坐标")
                return y
            elif coordinate == "coordinate":
                self.logger.info("获取当前窗口的x,y坐标")
                return x, y
            else:
                self.logger.error("参数输入有错")
        except:
            self.logger.error("获取当前窗口的坐标出现错误")

    # 将窗口移到指定坐标位置
    def moven_window(self, x, y):
        """
        将窗口移到指定坐标位置
        :param coordinate: x坐标 Y坐标
        """
        try:
            self.driver.set_window_position(x, y)
            self.logger.info(f"移动到坐标{x},{y}的位置")
        except:
            self.logger.error("将窗口移到所选位置出现错误")

    # 打开指定浏览器
    def open_browser(self,browser):
        """
        打开指定浏览器
        :param browser: 传浏览器类型的名称例如：chrome
        """
        browser=browser.capitalize()
        try:
            self.driver=getattr(webdriver,browser)()
            self.logger.info(f"打开{browser}浏览器")
        except:
            self.logger.info(f"无法打开浏览器,指定的浏览类型有误！")

# ----------------------------------------鼠标键盘的操作--------------------------------------------------------

    # 鼠标的单词操作method:click左键点击  context_click右键点击   double_click左键双击  move_to_element移动鼠标到指定元素 ,click_and_hold 点击并按住  release 松开释放
    def mouse(self,by,byvalue,method):
        """
        鼠标的操作：左键点击  右键点击  左键双击  移动鼠标到指定元素  点击按住   松开释放
        :param loc:  被鼠标操作的元素
        :param control: click左键点击  context_click右键点击   double_click左键双击  move_to_element移动鼠标到指定元素
                    click_and_hold 点击并按住  release 松开释放
        """
        try:
            el=self.locator(by,byvalue)
            getattr(ActionChains(self.driver),method)(el).perform()
            self.logger.info(f"元素鼠标操控{method}成功")
        except:
            self.logger.error(f"元素鼠标操控{method}失败")
            self.sava_page_shot("mouse")

    # 拖动元素，从元素一拖动元素二：传参第一个元素的定位，第二个元素的定位
    def drag_and_drop(self,oneby,onebyvalue,twoby,twobyvalue):
        try:
            first_element = self.locator(oneby,onebyvalue)
            second_element = self.locator(twoby,twobyvalue)
            ActionChains(self.driver).drag_and_drop(first_element, second_element)
            self.logger.info(f"从元素{first_element}拖动到元素{second_element}成功")
        except:
            self.logger.error(f"移动鼠标到指定元素成功")
            self.sava_page_shot("drag_and_drop")

    # 滑动某个元素，滑动到指定坐标
    def slid_element(self,first_element,x,y):
        try:
            ActionChains(self.driver).drag_and_drop_by_offset(first_element, x, y)
            self.logger.info(f"指定元素滑到坐标{x},{y}成功")
        except:
            self.logger.error(f"指定元素滑到坐标{x},{y}失败")
            self.sava_page_shot("slid_element")

# ----------------------------------------控件的操作--------------------------------------------------------

    # 下拉框的选择：方法选择control传：1.index通过下标选择   2.value通过value标签的名称选择  3.text通过下拉框内的文本选择
    def select_control(self, by,byvalue, control, value):
        """
        定位下拉框select中的值
        :param element: 元素定位
        :param control: 方法选择：1.index通过下标选择   2.value通过value标签的名称选择  3.text通过下拉框内的文本选择
        :param value: index：数字    value：值    text：文本
        """
        try:
            el = self.locator(by,byvalue)
            result = Select(el)
            if control == "index":
                result.select_by_index(value)
                self.logger.info(f"选择下拉框内{value}的值成功")
            elif control == "value":
                result.select_by_value(value)
                self.logger.info(f"选择下拉框内{value}的值成功")
            elif control == "text":
                result.select_by_visible_text(value)
                self.logger.info(f"选择下拉框内{value}的值成功")
            else:
                self.logger.error(f"输入的参数不正确，报错")
        except:
            self.logger.error(f"选择下拉框内{value}的值失败，出现错误")
            self.sava_page_shot("select_control")

    # 去掉指定元素
    def data_control(self, by,byvalue, tage_value ):
        """
        时间控件的操作，可以去掉指定标签中的属性值
        :param element: 元素定位对象
        :param tage_value: 需要去掉标签属性的名称   例如去掉'readonly'属性
        :param value:需要在控件填写的值
        """
        try:
            self.el = self.locator(by,byvalue)
            js = f"var el=arguments[0];el.removeAttribute('{tage_value}');"
            self.driver.execute_script(js, self.el)
            self.logger.info(f"成功去掉{self.el}的指定属性{tage_value}")
        except:
            self.logger.error(f"去掉{self.el}的指定属性{tage_value}，出现错误")
            self.sava_page_shot("data_control")

    # 滚动条的操控:1.loc_bottom：到指定元素的底部 2.loc_top到指定元素的顶部  3.bottom底部 4.top顶部
    def scroll_bar(self, by,byvalue,control,):
        """
        滚动条的操控  到顶部  到底部  到指定元素的顶部   到指定元素的底部
        :param type: 操控的方式 1.loc_bottom：到指定元素的底部 2.loc_top到指定元素的顶部  3.bottom底部 4.top顶部
        :param loc: 元素定位方式
        """
        try:
            self.el = self.locator(by,byvalue)
            if control == "loc_bottom":
                js = "arguments[0].scrollIntoView(false);"
                self.driver.execute_script(js, self.el)
                self.logger.info(f"操控元素{self.el}与页面的底部对齐，操作成功")
            elif control == "loc_top":
                el = self.locator(self.el)
                js = "arguments[0].scrollIntoView();"
                self.driver.execute_script(js, el)
                self.logger.info(f"操控元素{self.el}与页面的顶部对齐，操作成功")
            elif control == "bottom":
                self.driver.execute_script("scrollTo(document.body.scrollHeight,0)")
                self.logger.info(f"操控滚动条到底部完成，操作成功")
            elif control == "top":
                self.driver.execute_script("scrollTo(0,document.body.scrollHeight)")
                self.logger.info(f"操控滚动条到顶部完成，操作成功")
        except:
            self.logger.error(f"滚动条操作，出现错误")
            self.sava_page_shot("scroll_bar")

    # 针对windows控件中的上传文件操控，文件路径filePath
    def upload(self, filePath, browser_type="Chrome"):
        """
        针对windows控件中的上传文件操控
        :param filePath:
        :param browser_type:
        :return:
        """
        try:
            if browser_type == "Chrome":
                title = "打开"
            else:
                title = "文件上传"
            # FindWindow() 定位顶级 需要传顶级窗口的Class名称#32770 一级窗口
            dialog = win32gui.FindWindow("#32770", title)
            # 定位元素例如定位edit，那么需要一层一层的定位，FindWindowEx（）需要传父级和要定位层级的Class
            # 例如要定位ComboBoxEx32，那么需要传它的父级dialog 和 它本身的Class名称ComboBoxEx32
            ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)
            ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, "ComboBox", None)
            # edit在ComboBox下 ComboBox在ComboBoxEx32下  ComboBoxEx32在dialog下  一层一层定义
            edit = win32gui.FindWindowEx(ComboBox, 0, "Edit", None)
            # button在dialog所以只有一个父级也就是顶级
            button = win32gui.FindWindowEx(dialog, 0, "Button", None)
            # 往文件名编辑框中输入文件路径
            win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, filePath)
            # 上传操作
            win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 点击打开按钮
            self.logger.info(f"文件{filePath}上传成功")
        except:
            self.logger.error(f"文件{filePath}上传出现错误")
            self.sava_page_shot("upload")






if __name__ == '__main__':
    DD = BasePage(driver=webdriver)
    DD.open_browser("chrome")
    DD.run("open_url","https://kuxueedu.baijiayunxiao.com/adminstyle/login")
    DD.run("sleep", 2)
    DD.run("click", "xpath","//span[contains(text(),'密码登录')]")
    DD.run("input", "xpath", "//body/div[@id='app']/div[1]/div[2]/form[1]/div[1]/div[1]/div[2]/input[1]","15010671150")
    DD.run("sleep", 2)
    DD.run("input", "xpath", "//body/div[@id='app']/div[1]/div[2]/form[1]/div[2]/div[1]/div[1]/input[1]","abc123456")
    DD.run("sleep", 2)
    DD.run("click", "xpath", "//div[contains(text(),'立即登录')]")

    # time.sleep(3)
    # # DD.clicks("xpath","//span[contains(text(),'密码登录')]")
    # # DD.inputs("id","kw","星期一")
    # # driver  = webdriver.Chrome()
    # # el1 = driver.find_element(By.LINK_TEXT, "kw")
    # DD.locator(By.LINK_TEXT, "新闻")
    # DD.locator("By.LINK_TEXT", "新闻")
    # DD.locator("LINK_TEXT", "新闻")
    # DD.locator('link text', "新闻")
    # DD.locator("id","kw")