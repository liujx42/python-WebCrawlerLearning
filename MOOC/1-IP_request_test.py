#!/usr/bin/env python3
import requests

url = "http://m.ip138.com/ip.asp?ip="

try:
	uag = {'user-agent':'Chrome/66.0.3359.117'}
	r = requests.get(url+'202.204.80.112',headers=uag)
	r.raise_for_status()
	r.encoding = r.apparent_encoding
	print(r.text[-500:])

except:
	print("Wrong")

