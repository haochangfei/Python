# -*- coding:utf-8 -*-  
import re,os,os.path,time
import requests

##测试文件夹是否存在，如不存在则创建目标文件夹
dstDir=r'd:\yuanshi'
if not os.path.isdir(dstDir):
    os.mkdir(dstDir)

##通过url获取网页
startUrl=r'http://www.cae.cn/cae/html/main/col48/column_48_1.html'
myr=requests.get(startUrl)
myr.encoding='utf-8'
fp=myr.text

##利用正则，找到所有院士的链接
##打开fp或查看网页源码，得到要查找的为20160108142800035791989&columnid1=48" target="_blank">陈学东</a>
##分析该字符串，可以构造正则表达式即：'若干数字&columnid1=若干数字" target="_blank">若干字符</a>
pattern=r'(\d+)&columnid1=(\d+)" target="_blank">(.+)</a>'
##findall可以列出字符串中模式所有的匹配项，分析result的类型及结构，为包含元组的列表，元组元素为字符串
result=re.findall(pattern,fp)

for item in result:
    ##id1、id2为填充链接地址用，name是院士的名字，replace方法可以替换掉院士名字前后的<h3>或</h3>
    id1,id2,name=item
    name=name.replace('<h3>','').replace('</h3>','')
    ##生成保存后的文件路径级文件名，仅主文件名
    name=os.path.join(dstDir,name)
    ##生成每个院士的链接地址
    perUrl=r'http://www.cae.cn/cae/sites/main/jump.jsp?oid={0}&columnid1={1}'.format(id1,id2)
    newr=requests.get(perUrl)
    newr.encoding='utf-8'
    new_fp=newr.text
    time.sleep(0.2)       ##避免太快，如果抓取太频繁，服务器会拒绝
    ##抓取照片，分析可知图片地址为：img src="/cae/admin/upload/img/20160504155634976300642.jpg" style=
    ##构造正则表达式即'img src="/cae/admin/upload/若干字符" style='，findall中使用re.I是忽略大小写
    pattern=r'img src="/cae/admin/upload/(.+)" style='
    result=re.findall(pattern,new_fp,re.I)
    if result:
        ##将空格用%20替代
        picUrl=r'http://www.cae.cn/cae/admin/upload/{0}'.format(result[0].replace(' ',r'%20'))
        ##print u'抓取',name,u'照片',
        with open(name+'.jpg','wb') as pic:
            pic.write(requests.get(picUrl).content)
    ##抓取简介，分析院士简介在源码中的位置
    pattern=r'<p>(.+?)</p>'
    result=re.findall(pattern,new_fp)
    ##result中包含了院士的简介，但还有一些我们不需要的内容，需要进一步清除，以下代码可以演示result中的内容
    ##for i in result:
    ##    print i.encode('utf-8')
    ##result是包含字符串的列表，首先用回车将其连接成一个字符串，然后将字符串作为sub方法的第三个参数
    ##sub方法是在字符串（第三个参数）中用第二个参数替换第一个参数
    if result:
        intro=re.sub('(<a.+</a>)|(&ensp;)|(&nbsp;)','','\n'.join(result))
        ##print u'抓取',name,u'简介'
        with open(name+'.txt','w') as fff:
            fff.write(intro.encode('utf-8'))