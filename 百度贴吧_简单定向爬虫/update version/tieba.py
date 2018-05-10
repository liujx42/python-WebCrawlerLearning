#!/usr/bin/env python3
import requests
import re
import os
import time
from bs4 import BeautifulSoup
import random

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
		pageurls = re.findall('href="/p/[\d]*"',html)
		titles = re.findall('class=\"j_th_tit \">.*<',html)

		for i in range(len(pageurls)):
			title = titles[i].split('>')[1][:-1]
			pageurl = 'https://tieba.baidu.com' + pageurls[i].split('"')[1]
			ilt.append([pageurl,title])
	except:
		print('Wrong')
			
def sub_parsePage(ilt, filename):
	path = os.getcwd()
	phname = path + '/' + filename + '吧.txt'

	with open(phname,'w' ,encoding='utf-8') as f:
		for i in range(len(ilt)):
			time.sleep(round(random.uniform(0,5),2))
			newurl = ilt[i][0]
			newhtml = getHTMLText(newurl)
			newsoup = BeautifulSoup(newhtml,'html.parser')
			huifus = newsoup.find_all('div',class_='d_post_content j_d_post_content ')
			
			f.writelines(ilt[i][1] + '\n')
			count = 0
			for huifu in huifus:
				count = count + 1
				huifutext = huifu.get_text()
				huifutext.replace(' ','')
				huifutext.replace('\n','')
				f.writelines('(' + str(count) + ')' + huifutext + '\n')

				#这里只是将图片url存下来，未下载
				if huifu.find_all('img') != None:
					prcurls = huifu.find_all('img')
					for prcurl in prcurls:
						f.writelines('***' + prcurl['src'] + '***' + '\n')

			f.writelines('\n' + '-'*50 + '渲渲最可爱' + '-'*50 + '\n')

		f.close()
			
			
def main():
	time.sleep(3)
	filename = '闲鱼'
	start_url = "https://tieba.baidu.com/f?ie=utf-8&kw=" + filename + "&pn="
	depth = 1
	infoList = []
	
	for i in range(depth):
		try:
			url = start_url + str(i*50)
			html = getHTMLText(url)
			parsePage(infoList, html)
		except:
			continue
	sub_parsePage(infoList, filename)
			
if __name__ == '__main__':
	main()
	
