# _*_ coding:utf-8 _*_
# DATE 2021/8/27
import xlrd
from common.logger import log_error
from config import dir_config as dir

class ExcelUtil:

    #读取excel数据,为web自动化做数据驱动
    def read_excel(self,excel_path,sheet_name):
        """
        为web自动化的用例做数据驱动
        :param excel_path: 驱动文件的路径
        :param sheet_name: 驱动文件中sheet的名称
        :return:
        """
        xls = xlrd.open_workbook(dir.base_dir+excel_path,formatting_info=True)    # 先打开已存在的表，formatting_info=True表示保留原表格的样式
        sheet = xls.sheet_by_name(sheet_name)   # 通过sheet名称获得sheet对象
        keylist= []
        for rows in range(0, 1):  # 循环行
            for cols in range(0, sheet.ncols):
                keylist.append(sheet.cell_value(rows, cols))
        dataList = []
        for rows in range(1,sheet.nrows):#循环行
            info = {}
            tempList = []
            for cols in range(0,len(keylist)):#循环列，因为最后一列备注所以减1
                tempList.append(sheet.cell_value(rows,cols))
            for i in range(0, len(keylist)):
                info.setdefault(keylist[i], tempList[i])
            dataList.append(info)
        for i in dataList:
            if i["是否执行"] != "y":
                dataList.remove(i)
        return dataList


if __name__ == '__main__':
    print(ExcelUtil().read_excel("/testdatas/web/login_data.xls", "登录流程"))