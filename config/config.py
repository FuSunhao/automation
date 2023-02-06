# _*_ coding:utf-8 _*_
# DATE 2021/8/26

# 日志的配置文件
log_name="logs_"
log_level="INFO"
log_format='[%(asctime)s] %(filename)s->%(funcName)s line:%(lineno)d [%(levelname)s] %(message)s'

# 数据库配置
host = "49.232.31.190"
user = "root"
password = "abc152103"
database = "test"

# ---------------------测试用例汇总中的配置----------------
# 测试汇总用例工作表名称
casesSheet="测试用例汇总"
# 执行case的名称所在列数
casenameCol=4
# 是否执行用例所在列数
isexecuteCol=5
# 测试结果所在列数
casesresultCol=7

# --------------------测试用例中的配置-----------------------
# 获取关键字到操作值区域的数据
# 关键字所在类列数
keywordCol=3
# 操作值所在列数
actionCol=6
# 测试结果所在列数
stepresultCol=8
#用例运行时间所在列数
runtimeCol=7

# --------------------------------web---------------------------------------------
# 打开浏览器的类型
browsertype = "Chrome"
# browsertype = "Ie"
# browsertype = "Firefox"

# demo地址
base_url = "http://127.0.0.1/"

