# -*- coding: utf-8 -*-

import pandas as pd
import pymysql
from sqlalchemy import create_engine


class DBHelper(object):
    # 初始化mysql数据库链接
    def __init__(self, host_name='127.0.0.1', db_name='Test', user_name='root', pwd='P@ssw0rd'):
        self.engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}".format(host=host_name, db=db_name, user=user_name, pw=pwd))

    # 根据SQL语句进行数据库查询并返回查询结果
    def db_query(self, sql_query):
        with self.engine.connect() as conn:
            df = pd.read_sql_query(sql_query, conn)
        self.engine.dispose()
        # 为了演示方便，此处笔者直接返回了格式化后的测试数据
        # 在实际测试中，出于通用性的考虑，常直接返回df，然后测试时需再另行创建新的方法来处理结构化数据
        return df[["searchString", "expectString"]].values.tolist()


if __name__ == "__main__":
    db_reader = DBHelper()
    sql = '''select * from TestData'''
    print(db_reader.db_query(sql))
