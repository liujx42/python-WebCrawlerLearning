#!/usr/bin/env python3
import requests

url = "https://www.amazon.cn/dp/B004TUJ7A6/ref=sr_1_17?s=books&ie=UTF8&qid=1524562207&sr=1-17&keywords=python"

try:
	kv = {'user-agent':'Chrome/66.0.3359.117'}
	r = requests.get(url,headers=kv)
	print(r.request.headers)
	r.raise_for_status()
	r.encoding = r.apparent_encoding
	#print(r.text[1000:2000])
except:
	print("Wrong")

