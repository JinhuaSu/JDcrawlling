import urllib.request
import requests
import time 
import json
from lxml import etree
import pickle
import re
requests.adapters.DEFAULT_RETRIES = 5 # 增加重连次数
s = requests.session()
s.keep_alive = False
def legal(s):
	s = s.replace(' ','')
	s = s.replace('(','')
	s = s.replace(')','')
	s = s.replace('（','')
	s = s.replace('）','')
	s = s.replace('/','')
	return s
def get_detail_dict(detail):
	detail_dict = {}
	block_list=['入网型号','屏占比','运营商标志或内容','屏幕像素密度（ppi）','摄像头数量','电池是否可拆卸','无线充电','副SIM卡4G网络','4G网络','SIM卡类型']
	while len(detail)>1:
		pop = detail.pop(0)
		if pop[0]=='\n':
			continue
		elif pop in block_list:
			tmp = detail.pop(0)
			while tmp[0] == '\n':
				tmp = detail.pop(0)
		tmp = detail.pop(0)
		while tmp[0] == '\n':
			tmp = detail.pop(0)
		pop = legal(pop)
		detail_dict[pop] = tmp
	return detail_dict
def get_json_dict(ID,headers):
	url_c = 'https://club.jd.com/comment/productCommentSummaries.action?referenceIds='
	url_p = 'https://p.3.cn/prices/mgets?skuIds=J_'
	url = url_c + ID
	response1 = requests.get(url,headers=headers)
	dic1 = json.loads(response1.content.decode("utf-8","ignore"))['CommentsCount'][0]
	url = url_p + ID
	response2 = requests.get(url,headers=headers)
	dic2 = json.loads(response2.content[1:-2])
	dic1.update(dic2)
	return dic1 
def one_phone(args,url,headers):
	ID = url.split('/')[-1][:-5]
	request = urllib.request.Request(url,headers=headers)
	html = urllib.request.urlopen(request).read()
	content = etree.HTML(html)
	try:
		store = content.xpath('//div[@class="item"]/div[@class="name"]/a/text()')[0]
	except:
		store = None
	print(store)
	detail_key = content.xpath('//dl[@class="clearfix"]//dt/text()')
	detail_value = content.xpath('//dl[@class="clearfix"]//dd[last()]/text()')
	#detail = get_detail_dict(detail)
	detail = dict(zip(detail_key,detail_value))
	json_dic = get_json_dict(ID,headers)
	json_dic.update(detail)
	res_dic = {"UNIKEY":ID,'url':url,'store':store}
	res_dic.update(json_dic)
	return res_dic

if __name__=="__main__":
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
	url = "https://item.jd.com/100003395467.html"
	args = 'test'
	row = one_phone(args,url,headers)
	print(row)
	with open('result/row.pk','wb') as f:
		pickle.dump(row,f)
