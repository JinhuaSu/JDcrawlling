import pymysql
import pickle
from sql_tool import *
import argparse
from util.logging import logger,init_logger
init_logger('logs/test')
parser = argparse.ArgumentParser(description='A3C')
parser.add_argument('--mode',default ='crawl',choices=['crawl','debug'])
parser.add_argument('--log_file',default ='logs/output')
parser.add_argument('--map_file',default ='result/map_dict.pk')
parser.add_argument('--columns_file',default ='result/major_list.pk')
parser.add_argument('--table_name',default ='JDphone_raw')
parser.add_argument('--begin',default ='1')
parser.add_argument('--end',default ='1')

args = parser.parse_args()
mysql_tool = mysql_tool(args,'localhost','root','20192019_yhf',3306,'spiders',logger)

with open('result/row.pk','rb') as f:
	row = pickle.load(f)

mysql_tool.auto_save_data(row,'JDphone_raw')
db = pymysql.connect(host='localhost',user='root',password='20192019_yhf',port=3306,database='spiders')
cursor =db.cursor()
res = cursor.execute('select * from JDphone_raw')
print(res)
