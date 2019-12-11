# haha
import urllib.request
import requests
import time 
from lxml import etree
import re

def jdPhone_spider(url,beginPage,endPage):
	for page in range(beginPage,endPage+1):
		pn = page*2 - 1
		print("crawlling No,",page,"page")
		fullurl = url+"&page="+str(pn)
		time.sleep(2)
		load_page(fullurl)

def load_page(url):
	#headers = {"user_agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
	#}

	#request = urllib.request.Request(url,headers=headers)
	#html = urllib.request.urlopen(request).read()
	#print(html)
	# The Headers re
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
	print(len(content_list))
	for i in range(1,31):
		try:
			result = re.split(r":",content_list[i-1])[1]
			if i == 1:
				print(result)
			content_list[i-1] = result
		except Exception as e:
			continue
	for j in content_list:
		new_url = "http:" + j 
		load_link_page(new_url,headers)
		count_l.append(new_url)

def load_link_page(url,headers):
	request = urllib.request.Request(url,headers=headers)
	html = urllib.request.urlopen(request).read()
	content = etree.HTML(html)
	brand = content.xpath('//div[@class="p-parameter"]/ul[@id="parameter-brand"]/li/@title')

if __name__ == '__main__':
	beginPage = int(input("please enter the startPage:"))
	endPage = int(input("please enter the endPage:"))
	url = "https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8"
	jdPhone_spider(url,beginPage,endPage)
	#headers = {
	#'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0',
	#'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
	#'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.5,zh;q=0.3',
	#'Referer': 'https://www.jd.com/',
	#'DNT': '1',
	#'Connection': 'keep-alive',
	#'Upgrade-Insecure-Requests': '1',
	#'TE': 'Trailers',
	#}

	#params = (
	#('keyword', '手机'),
	#('enc', 'utf-8'),
	#('wq', '手机'),
	#('pvid', '70b2126fcf3246ce9f32710d41799ede'),
	#)

	#response = requests.get(url,headers=headers, params=params)
	#print(url)
	#html = response.content
	#content = etree.HTML(html)
	#content_list = content.xpath('//div[@class="gl-i-wrap"]/div[@class="p-img"]/a/@href')
	#print(content_list)
