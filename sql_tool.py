import pymysql
import pickle
def legal(s):
	s = s.replace(' ','')
	s = s.replace('(','')
	s = s.replace(')','')
	s = s.replace('（','')
	s = s.replace('）','')
	s = s.replace('/','')
	return s 
class mysql_tool(object):
	def __init__(self,args, host, user,passwd,port,db):
		self.args = args
		self.db = pymysql.connect(host=host,user=user,password=passwd,port=port,database=db)
		with open(args.map_file,'rb') as f:
			self.map = pickle.load(f)
		with open(args.columns_file,'rb') as f:
			self.columns = pickle.load(f)
		self.columns.remove('网络频率（2G/3G）')
		self.auto_create_table(self.columns,args.table_name)
		
	def auto_create_table(self,columns,name):
		sql = 'CREATE TABLE IF NOT EXISTS %s (' % name
		unikey = 'UNIKEY'
		for key in columns:
			key = legal(key)
			sql += key + ' VARCHAR(100), '
		sql += 'PRIMARY KEY (%s))' % unikey
		cursor = self.db.cursor()
		try:
			print(sql)
			cursor.execute(sql)
			self.db.commit()
		except:
			self.db.rollback()
			raise 'create table fail!'
		cursor.close()
	def auto_save_data(self,row,table):
		clear_columns = [legal(s) for s in self.columns]
		new_row = dict(zip(clear_columns,[None] * len(row)))
		for key,value in row.items():
			try:
				if key in self.columns:
					new_row[legal(key)] = value
				elif key != '网络频率（2G/3G）' and key in self.map.keys() and self.map[key]!= None and new_row[self.map[key]] == None:
					new_row[legal(self.map[key])] = value
			except:
				print('keyErorr:',key)
		keys = ', '.join(new_row.keys())
		values = ', '.join(['%s']*len(new_row))
		sql='INSERT INTO {table} ({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE'.format(table = table,keys =keys,values = values)
		update = ','.join([" {key} = %s".format(key=key) for key in new_row.keys()])
		sql += update
		cursor = self.db.cursor()
		try:
			cursor.execute(sql,tuple(list(new_row.values())+list(new_row.values())))
			self.db.commit()
			print('save data successful')
		except:
			print('save data failed')
			print(sql)
			self.db.rollback()
		cursor.close()
if __name__ == '__main__':
	mysql_tool = mysql_tool(None,'localhost','root','20192019_yhf',3306,'spiders')
	mysql_tool.auto_create_table({'湖滨饭店':'dad','dads':'dasds'},'test')
