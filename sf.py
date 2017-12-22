# -*- coding:utf-8 -*-  
import re,os,os.path,time
import requests


sdir=r'd:\note'
if not os.path.isdir(sdir):
    os.mkdir(sdir)

startUrl=r'http://www.17k.com/list/2677728.html'
myr=requests.get(startUrl)
myr.encoding='utf-8'
fp=myr.text
##print fp

num=0

pattern2=r'<a target="_blank" href="/chapter/2677728/(.+).html"'
result2=re.findall(pattern2,fp)
for i in result2:
    if i=='29954028':
        continue
    if i=='33570318':
        continue
    if i=='33575402':
        break
    num=num+1
    name='chapter'+str(num)
    name=os.path.join(sdir,name)
    time.sleep(0.2)
    url=r'http://www.17k.com/chapter/2677728/{0}.html'.format(i)
    myr=requests.get(url)
    myr.encoding='utf-8'
    fp=myr.text
    pattern3=r''
##  print i
##    print fp
    pat=r'<div class="p">([\w\W]*)<div class="author-say"></div>'
    result3=re.findall(pat,fp)
    s=result3[0].encode('utf-8')
    t=s.replace(r'&#12288;&#12288;','').replace(r'<br /><br />','')
##    print t
    with open(name+'.txt','w') as fff:
        fff.write(t)
    




