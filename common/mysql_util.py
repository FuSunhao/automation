# _*_ coding:utf-8 _*_
# DATE 2021/9/7
import traceback
import pymysql
import pymysql.cursors
from common.logger import  log_error,log_info
from config import config

"""
安装第三方库pymysql
数据库：存储项目数据     验证数据---》代码取数据库的数据来跟实际结果进行比对
1、连接数据库
2、创建流标实例
3、调用游标实例的excute(sql)    excute(sql,(values),bool)  sql语句   数据库表常见操作
"""

# 1、连接数据库服务
class MysqlENC:
    host = config.host
    user = config.user
    password = config.password
    database = config.database
    def __init__(self):
        self.conn = self.connect()
    """连接数据库"""
    def connect(slef):
        try:
            conn=pymysql.connect(
                host= MysqlENC.host,
                user= MysqlENC.user,
                passwd=MysqlENC.password,
                db= MysqlENC.database
            )
            return  conn
        except Exception as f:
            log_error("数据库连接异常：%s" % str(traceback.format_exc()))

    """数据库查询语句"""
    def select(self, sql):
        try:
            # 获取游标实例，加上cursor=pymysql.cursors.DictCursor返回的是字典形式，不加返回的是正常形式
            cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
            # 执行sql语句
            # db.select_showall("select * from user")
            cursor.execute(sql)
            # 查看所有返回结果
            allrows = cursor.fetchall()
            log_info("查询结果是：%s" % allrows)
            return allrows


            # 返回第一条记录
            # onerow = cursor.fetchone()
            # return onerow

            # 返回多条记录
            # manyrow = cursor.fetchmany(3)
            # return manyrow
        except Exception as f:
            log_error("数据库查询异常：%s" % str(traceback.format_exc()))
    """插入单条数据到表中"""
    def insert(self,sql):
        try:
            # 获取游标实例，加上cursor=pymysql.cursors.DictCursor返回的是字典形式，不加返回的是正常形式
            cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
            # 执行sql语句
            cursor.execute(sql)
            # 提交保存操作（修改，删除，插入都需要提交保存）
            self.conn.commit()
            # 查看返回的结果
            rowcount=cursor.rowcount
            log_info(f"{rowcount}行记录插入成功！")
            return rowcount
        except Exception as f:
            log_error("数据库插入异常：%s" % str(traceback.format_exc()))

    """修改数据"""
    def update(self, sql):
        try:
            # 获取游标实例
            cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
            # 执行sql语句
            # update("update user set classname = 'yiban'")
            cursor.execute(sql)
            # 提交保存操作（修改，删除，插入都需要提交保存）
            self.conn.commit()
            # 查看返回的结果
            rowcount = cursor.rowcount
            log_info(f"{rowcount}行记录执行成功！")
            return rowcount
        except Exception as f:
            log_error("数据库修改异常：%s" % str(traceback.format_exc()))

    """删除数据"""
    def delete(self, sql):
        try:
            # 获取游标实例
            cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
            # 执行sql语句
            cursor.execute(sql)
            # 提交保存操作（修改，删除，插入都需要提交保存）
            self.conn.commit()
            # 查看返回的结果
            rowcount = cursor.rowcount
            log_info(f"{rowcount}行记录执行成功！")

            return rowcount
        except Exception as f:
            log_error("数据库删除异常：%s" % str(traceback.format_exc()))



    def assert_dict(self,methon,sql,expected=None):
        """
        数据结构断言验证，成功返回True,失败返回False
        :param methon: 传入方法名称，select/insert/update/delete
        :param sql: 执行sql的语句
        :param expected: 预期的值，只有select使用  expected格式例如{'ENAME': '杨希'}
        :return:
        """
        if methon == "select":
            try:
                result = self.select(sql)
                for data in result:
                    for key in expected:
                        if (key in data) & (data[key] == expected[key]):
                            return True
                        else:
                            return False
            except:
                log_error("查询断言出现错误")
        elif methon == "insert":
            try:
                result = self.insert(sql)
                if result != 0:
                    return True
                else:
                    return False
            except:
                log_error("查询断言出现错误")
        elif methon == "update":
            try:
                result = self.update(sql)
                if result != 0:
                    return True
                else:
                    return False
            except:
                log_error("查询断言出现错误")
        elif methon == "delete":
            try:
                result = self.delete(sql)
                if result != 0:
                    return True
                else:
                    return False
            except:
                log_error("查询断言出现错误")
        else:
            log_error("输入的参数有误")

if __name__ == '__main__':
    # MysqlENC().mysqlassert("select * from emp where ename = '杨希'")
    eee = {'EMPNO': 7369, 'ENAME': '杨希', 'JOB': '人事', 'MGR': 7902, 'HIREDATE': 'datetime.date(1980, 12, 17)',
           'SAL': 800.0, 'COMM': None, 'DEPTNO': 20}
    selectvalue = {'ENAME': '杨希'}
    print(MysqlENC().assert_dict("insert", "insert into dept (DEPTNO,DNAME,LOC) values (100,'老33233儿','二33323二');", 1))