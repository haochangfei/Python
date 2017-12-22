# -*- coding:utf-8 -*-
import requests,re
from bs4 import BeautifulSoup
##http://beautifulsoup.readthedocs.io/zh_CN/latest/    Beautiful Soup 4.4.0 文档

def getreq(url):##得到url的code
    myreq = requests.get(url)
    myreq.encoding='utf-8'
    return myreq.text

def findValuable(fp):##在网页code中查找可以使用的url
    soup=BeautifulSoup(fp,"html.parser")
    a=soup.findAll(name='a',attrs={"href":re.compile(r'^http:')})
    for i in a:
       print i.get('href')
        
startUrl="http://www.bztc.edu.cn"
fp = getreq(startUrl)
findValuable(fp)

