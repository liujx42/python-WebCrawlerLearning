#!/usr/bin/env python3
import requests
import re
import os
import time

def getHTMLText(url):
	try:
		r = requests.get(url, headers={'user-agent':'Chrome/66.0.3359.117'})
		r.raise_for_status()
		r.encoding = 'utf-8'
		return r.text
	except:
		return ""
		
def parsePage(ilt, html):
	try:
		times = re.findall(r'title=\"创建时间\">[\d]*[-:][\d]*',html)
		titles = re.findall('class=\"j_th_tit \">.*<',html)
		huifus = re.findall('\"回复\">.*<',html)

		for i in range(len(times)):
			timels = times[i].split('>')[1]
			
			match = re.match(r'[\d]*:[\d]*',timels)
			if match:
				timels = time.strftime('%Y-%m-%d', time.localtime())
				
			match = re.match(r'[\d]{1,2}-[\d]*',timels)
			if match:
				timels = time.strftime('%Y-', time.localtime()) + timels
				
			title = titles[i].split('>')[1][:-1]
			huifu = huifus[i].split('>')[1][:-1]
			ilt.append([timels, title, huifu])
	except:
		print('Wrong')
			
def printGoodsList(ilt, filename):
	path = os.getcwd()
	phname = path + '\\' + filename + '吧.txt'	
	tplt = "{:^4}\t{:<10}\t{:<10}\t{:<60}\n"
	count = 0		
	with open(phname,'w' ,encoding='utf-8') as f:
		f.writelines(tplt.format('序号','时间','回复','标题'))
		for g in ilt:
			count = count + 1
			f.writelines(tplt.format(count,g[0],g[2],g[1]))	
		f.close()
		print('Sucessed')
			
def main():
	time.sleep(3)
	filename = '租车'
	start_url = "https://tieba.baidu.com/f?ie=utf-8&kw=" + filename + "&pn="
	depth = 2
	infoList = []
	
	for i in range(depth):
		try:
			url = start_url + str(i*50)
			html = getHTMLText(url)
			parsePage(infoList, html)
		except:
			continue
	printGoodsList(infoList, filename)
			
if __name__ == '__main__':
	main()
	
