#!/usr/bin/env python3
import requests

url = "https://www.baidu.com/s"

try:
	kv = {'wd':'python'}
	uag = {'user-agent':'Chrome/66.0.3359.117'}
	r = requests.get(url,params=kv,headers=uag)
	print(r.request.url)
	r.raise_for_status()
	r.encoding = r.apparent_encoding
	print(r.text[:1000])
except:
	print("Wrong")

