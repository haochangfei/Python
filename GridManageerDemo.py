# -*- coding:utf-8 -*-
from Tkinter import *
class GridManagerDemo():
    window=Tk()
    window.title("Grid Manageer Demo")
    message=Message(window,text="This Message widget occupies three rows and two columns")
    message.grid(row=1,column=1,rowspan=3,columnspan=2)
    ##message放置在1行1列，然后扩展3行2列，rowspan和columnspan是行列的跨度
    Label(window,text="First name:").grid(row=1,column=3)
    Entry(window).grid(row=1,column=4,padx=5,pady=5)
    ##padx和pady表示组件外部在x(y)方向上填充的空间大小，
    Label(window,text="Last name:").grid(row=2,column=3)
    Entry(window).grid(row=2,column=4)
    Button(window,text="Get Name").grid(row=3,padx=5,pady=5,column=4,sticky=E)
    ##sticky是表示组件紧靠所在单元格的某一边角，常用值有N、S、W、E、NW、SW、SE、NE
    window.mainloop()
GridManagerDemo()
