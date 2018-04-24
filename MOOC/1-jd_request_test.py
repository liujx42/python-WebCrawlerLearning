#!/usr/bin/env python3
import requests

url = "https://item.jd.com/26638144664.html#crumb-wrap"

try:
	r = requests.get(url)
	r.raise_for_status()
	r.encoding = r.apparent_encoding
	print(r.text[:1000])
except:
	print("Wrong")

