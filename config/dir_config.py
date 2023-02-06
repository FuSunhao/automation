# _*_ coding:utf-8 _*_
# DATE 2021/8/26
import os

# 根路径
base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 测试报告路径
reports_dir=os.path.join(base_dir,"Outputs/reports/")
# 日志路径
logs_dir=os.path.join(base_dir,"logs/")
# 失败截图
screen_dir=os.path.join(base_dir,"Outputs/screenshots/")
# 接口关联存储文件extract.yam
extract_dir=os.path.join(base_dir,"testdatas/api/")
# 测试数据配置文件文件config_yml
config_yml_dir=os.path.join(base_dir,"testdatas/")
# web_testdatas的数据文件
web_testdatas_dir = os.path.join(base_dir,"testdatas/web/demo/")


if __name__ == '__main__':
    print(base_dir)