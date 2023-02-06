# _*_ coding:utf-8 _*_
# DATE 2021/8/26
import os
import pytest


if __name__ == '__main__':
    # 执行所有的测试用例的主方法
    pytest.main()
    # 生成allure报告
    os.system("allure generate ./outputs/temp -o ./outputs/reports --clean")

# //第二个版本