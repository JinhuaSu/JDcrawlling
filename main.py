from crawl_phone_page import *
from sql_tool import *
import urllib.request
import requests
import time 
from lxml import etree
import re
import argparse
import pickle
from util.logging import logger,init_logger

def jdPhone_spider(args,url,beginPage,endPage):
	for page in range(beginPage,endPage+1):
		pn = page*2 - 1
		print("crawlling No,",page,"page")
		fullurl = url+"&page="+str(pn)
		time.sleep(2)
		load_page(args,fullurl)

def load_page(args,url):
	global mysql_tool
	global phone_num
	global tmp_dict
	headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
	'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.5,zh;q=0.3',
	'Referer': 'https://www.jd.com/',
	'DNT': '1',
	'Connection': 'keep-alive',
	'Upgrade-Insecure-Requests': '1',
	'TE': 'Trailers',
	}

	params = (
	('keyword', '手机'),
	('enc', 'utf-8'),
	('wq', '手机'),
	('pvid', '70b2126fcf3246ce9f32710d41799ede'),
	)

	response = requests.get(url,headers=headers, params=params)
	html = response.content
	content = etree.HTML(html)
	content_list = content.xpath('//div[@class="gl-i-wrap"]/div[@class="p-img"]/a/@href')

	for i in range(1,31):
		try:
			result = re.split(r":",content_list[i-1])[1]
			content_list[i-1] = result
		except Exception as e:
			continue
	for j in content_list:
		new_url = "http:" + j 
		logger.info('trying to crawling No. %s phone info...' % phone_num )
		phone_num += 1
		row = one_phone(args,new_url,headers)
		print(len(row))
		if args.mode == 'debug':
			tmp_dict[row['UNIKEY']] = row
		else:
			mysql_tool.auto_save_data(row,args.table_name)
			phone_num += 1

parser = argparse.ArgumentParser(description='A3C')
parser.add_argument('--mode',default ='crawl',choices=['crawl','debug'])
parser.add_argument('--log_file',default ='logs/output')
parser.add_argument('--map_file',default ='result/map_dict.pk')
parser.add_argument('--columns_file',default ='result/major_list.pk')
parser.add_argument('--table_name',default ='JDphone_raw')
parser.add_argument('--begin',default ='1')
parser.add_argument('--end',default ='1')

if __name__ == '__main__':
	args = parser.parse_args()
	init_logger(args.log_file)
	beginPage = int(args.begin)
	endPage = int(args.end)
	url = "https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8"
	global mysql_tool
	mysql_tool = mysql_tool(args,'localhost','root','20192019_yhf',3306,'spiders')
	global phone_num
	phone_num = 1
	global tmp_dict
	tmp_dict = {}
	jdPhone_spider(args,url,beginPage,endPage)
	if args.mode == 'debug':
		with open('result/debug.pk','wb') as f:
			pickle.dump(tmp_dict,f)
	
