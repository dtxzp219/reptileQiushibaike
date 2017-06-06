#!/usr/bin/env 
# -*- coding:utf-8 -*-
# import urllib2
# response=urllib2.urlopen("http://www.baidu.com")
# print response.read();

import urllib
import urllib2
import re
import os
import json

page=2
url='http://www.qiushibaike.com/8hr/page/%s/?s=4988835'%(str(page))
user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
headers={'User-Agent':user_agent};



print(url);



def createDocuments():
#获取当前文件所在的绝对路径
	print os.path.abspath(' ')
#在当前目录下创建一个新的文件夹
	absPath=os.path.abspath('')
#先将要创建的路径拼出来 注如果直接拼接字符串 在不同的操作系统上可能有不同的分隔符
	cratePath= os.path.join(absPath,'duanzi')
	print cratePath
	if os.path.isdir(cratePath) == True:
		print '已经存在'
	else:
		os.mkdir(cratePath)
	return cratePath



def saveFile(url,path,name):
	f=open(path+'/'+str(name)+'.jpg',"wb")
	# print path+'/'+url
	req=urllib2.urlopen(url)
	buf=req.read()
	f.write(buf)

# saveFile('3123123.jpg', path)

path= createDocuments();

try:
	request=urllib2.Request(url,headers=headers);
	respponse=urllib2.urlopen(request);
	content=respponse.read().decode('utf-8')
	# pattern=re.compile(r'<div class="content">.*?<span>(.*?)</span>.*?</div>',re.S)
	# items=re.findall(pattern,content);
	# for item in items:
	# 	print item
# <a .*?>.*?<img src="(.*?)" alt=.*?"/>.*?</a>
	images=re.compile(r'<a.*?<img src="(//pic.qiushibaike.*?)" alt=.*?"/>.*?</a>',re.S)
	imageList=re.findall(images, content)
	print json.dumps(imageList)
	x=0
	for imageUrl in imageList:
		print '最后一个:'+str(x)+'zongg'

		url='http:'+imageUrl.decode('utf-8')
		print url

		saveFile(url,path,x)
		x=x+1

except Exception as e:
	raise e


