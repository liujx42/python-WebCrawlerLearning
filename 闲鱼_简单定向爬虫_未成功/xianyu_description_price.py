#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import bs4
import re
import os

def getHTMLText(url):
	try:
		r = requests.get(url,
                                 headers={
                                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                                        'Accept-Encoding': 'gzip, deflate, br',
                                        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
                                        'Cache-Control': 'no-cache',
                                        'Connection': 'keep-alive',
                                        'Upgrade-Insecure-Requests': '1',
                                        'user-agent':'"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_1 like Mac OS X; ja-jp) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 Mobile/8B117 Safari/6531.22.7"'})
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text
	except:
		return ""
		
def parsePage(ilt, html):
	try:
		soup = BeautifulSoup(html, 'html.parser')
		print(soup)
		for ibs in soup('item-brief-desc'):
			desc = ibs.text
			primat = ibs.parent.previous_sibling.find(re.compile('[\d\.]*'))
			price = primat.group(0)
			print(price)
			ilt.append([desc, title])
	except:
		print('Wrong')
			
def printGoodsList(ilt, filename):
	path = os.getcwd()
	phname = path + '\\' + filename + '_描述与价格.txt'	
	tplt = "{:4}\t{}\t{}\n"
	count = 0		
	with open(phname,'w') as f:
		f.writelines(tplt.format('序号','描述','价格'))
		for g in ilt:
			count = count + 1
			f.writelines(tplt.format(count,g[0],g[1]))	
		f.close()
		print('Sucessed')
			
def main():
	filename = '闲鱼'
	start_url = "https://s.2.taobao.com/list/list.htm?catid=57170002&oon=10&page="
	depth = 1
	infoList = []
	
	for i in range(depth):
		try:
			url = start_url + str(i+1)
			html = getHTMLText(url)
			parsePage(infoList, html)
		except:
			continue
	printGoodsList(infoList, filename)
			
if __name__ == '__main__':
	main()
	
