import json
import urllib.request
import requests
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
url_c = 'https://club.jd.com/comment/productCommentSummaries.action?referenceIds='
url_p = 'https://p.3.cn/prices/mgets?skuIds=J_'
#ID = '100003395467'
ID ='56745178469'
url = url_c + ID
response = requests.get(url,headers=headers)
#print(response.content)
dic = json.loads(response.content)['CommentsCount'][0]
print(dic)
url = url_p + ID
response = requests.get(url,headers=headers)
print(response.content)
dic = json.loads(response.content[1:-2])
print(dic)
