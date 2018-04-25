#!/usr/bin/env python3
import requests
import re
import os

def getHTMLText(url):
	try:
		r = requests.get(url, headers={'user-agent':'Chrome/66.0.3359.117'})
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text
	except:
		return ""
		
def parsePage(ilt, html):
	try:
		plt = re.findall('\"view_price\"\:\"[\d\.]*\"',html)
		tlt = re.findall('\"raw_title\"\:\".*?\"',html)
		for i in range(len(plt)):
			price = eval(plt[i].split(':')[1])
			title = eval(tlt[i].split(':')[1])
			ilt.append([price, title])
	except:
		print('Wrong')
			
def printGoodsList(ilt, goods):
	path = os.getcwd()
	phname = path + '\\3-' + goods + '_淘宝价格.txt'	
	tplt = "{:4}\t{:8}\t{:16}\n"
	count = 0		
	with open(phname,'w') as f:
		print(tplt.format('序号','价格','商品名称'))
		f.writelines(tplt.format('序号','价格','商品名称'))
		for g in ilt:
			count = count + 1
			print(tplt.format(count,g[0],g[1]))
			f.writelines(tplt.format(count,g[0],g[1]))	
		f.close()
		print('Sucessed')
			
def main():
	goods = '书架'
	start_url = "https://s.taobao.com/search?q=" + goods
	depth = 3
	infoList = []
	
	for i in range(depth):
		try:
			url = start_url + '&s=' + str(44*i)
			html = getHTMLText(url)
			parsePage(infoList, html)
		except:
			continue
	printGoodsList(infoList, goods)
			
if __name__ == '__main__':
	main()
	