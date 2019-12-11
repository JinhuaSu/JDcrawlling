import pymysql

db = pymysql.connect(host='localhost',user='root',password='20192019_yhf',port=3306,database='spiders')
cursor =db.cursor()
res = cursor.execute('select * from JDphone_raw')
print(res)
