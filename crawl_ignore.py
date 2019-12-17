import urllib.request
import pymysql
import requests
import time 
import json
from lxml import etree
import pickle
import re
requests.adapters.DEFAULT_RETRIES = 5 # 增加重连次数
s = requests.session()
s.keep_alive = False
url = 'https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv36&productId=%s&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1'
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
	'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.5,zh;q=0.3',
	'Referer': 'https://www.jd.com/',
	'DNT': '1',
	#'Connection': 'keep-alive',
	'Upgrade-Insecure-Requests': '1',
	'TE': 'Trailers',
	}
db = pymysql.connect(host='10.224.0.11',user='root',password='20192019_yhf',port=3306,database='spiders')
cursor = db.cursor()
with open('result/ignore_dict.pk','rb') as f:
	ignore_key = pickle.load(f)
while True:
	UNIKEY = str(ignore_key[-1])
	response = requests.get(url % UNIKEY,headers=headers)
	dic = json.loads(response.text[24:-2])
	data = ','.join([item['name']+':'+str(item['count']) for item in dic['hotCommentTagStatistics']])
	print(data)
	sql2 = "update JDphone_comment set HOTWORDS=%s WHERE UNIKEY=%s;"
	print(cursor.execute(sql2, (data,UNIKEY)))
	db.commit()
	ignore_key.pop()
	print('fail!')
		
	#request = urllib.request.Request(url,headers=headers)
#html = urllib.request.urlopen(request).read()
#print(html)
#content = etree.HTML(html) 
