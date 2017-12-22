# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup


def getWebText(url):
    req = requests.get(url)
    req.encoding = "utf-8"
    return req.text

url = "http://www.bztc.edu.cn/"
text = getWebText(url)
##print type(text)
soup = BeautifulSoup(text,"html.parser")
link = soup.find("a")

print link



