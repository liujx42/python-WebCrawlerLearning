#!/usr/bin/env python3
import requests
import os

url = "http://pic29.photophoto.cn/20131204/0034034499213463_b.jpg"
path = os.getcwd()
phname = path + '\\' + url.split('/')[-1]

try:
	uag = {'user-agent':'Chrome/66.0.3359.117'}
	r = requests.get(url,headers=uag)
	r.raise_for_status()
	
	with open(phname,'wb') as f:
		f.write(r.content)
		f.close()
		print('Sucessed')
except:
	print("Wrong")

