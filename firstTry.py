# -*- coding:utf-8 -*-
import requests
import re
from bs4 import BeautifulSoup


def getWebText(url):
    req = requests.get(url)
    req.encoding = "utf-8"
    return req.text

def findValuable(fp):##在网页code中查找可以使用的url
    soup=BeautifulSoup(fp,"html.parser")
    a=soup.findAll(name='a',attrs={"href":re.compile(r'^http:')})
    for i in a:
        print (i.get('href'))

url = "http://www.bztc.edu.cn/"
fp = getWebText(url)
findValuable(fp)



