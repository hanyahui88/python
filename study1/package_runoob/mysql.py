# -*- coding: UTF-8 -*-
# mysqldb模块 没有安装成功
import pymysql


def selectone():
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='books', charset='utf8')
    cursor = conn.cursor()
    cursor.execute("select * from t_sys_dic")
    data = cursor.fetchone()
    printData(data)
    conn.close()
    return data


def selectall():
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='books', charset='utf8')
    cursor = conn.cursor()
    cursor.execute("select * from t_sys_dic")
    data = cursor.fetchall()
    printData(data)
    conn.close()
    return data


def selectmany():
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='books', charset='utf8')
    cursor = conn.cursor()
    cursor.execute("select * from t_sys_dic")
    data = cursor.fetchmany()
    printData(data)
    conn.close()
    return data


def printData(data):
    for row in data:
        id = row[0]
        age = row[1]
        name = row[2]
        print(id, age, name)


def createdb():
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='books', charset='utf8')
    cursor = conn.cursor()
    sql = """
        create table t_python(id int(11) NOT NULL,age int(11) NOT NULL,name VARCHAR(20) NOT NULL)
    """
    cursor.execute(sql)
    conn.close()


def insert():
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='books', charset='utf8')
    cursor = conn.cursor()
    sql = """insert into t_python values(1,11,'alvin')"""
    # 或者
    # sql = """insert into t_python values('%d','%d','%s') % (1,11,'alvin')"""
    try:

        cursor.execute(sql)
        conn.commit()
    except RuntimeError:
        conn.rollback()

    conn.close()


selectall()
