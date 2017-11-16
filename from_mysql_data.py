import pymysql
import pandas as pd
import numpy as np

#connect to mysql
db = pymysql.connect(host="localhost",port=3306,user="root",passwd="root",db="即时确认率月报",charset="gbk")
#建立游标
cursor = db.cursor()
#写入sql语句
sql = """SELECT `省长`,`区域`,`族别`,`月份`,sum(`订单量`) FROM zhanqu2017 GROUP BY `省长`,`区域`,`族别`,`月份`"""
cursor.execute(sql) #执行
results = cursor.fetchall() #提取数据
results_array = np.array(results) #转换为array
results_df = pd.DataFrame(results_array) #转换为数据框
results_df.to_csv("rqy.csv",encoding="gbk") #导出
#关闭数据库
db.close()
