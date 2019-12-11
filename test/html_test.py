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

params = (
('keyword', '1000x'),
('enc', 'utf-8'),
('wq', '1000x'),
('pvid', '70b2126fcf3246ce9f32710d41799ede'),
)

response = requests.get('https://search.jd.com/Search', headers=headers, params=params)
print(response)
