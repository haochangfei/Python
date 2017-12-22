# -*- coding:utf-8 -*-
from Tkinter import *
class PackManagerDemoWithSide():
    window=Tk()
    window.title("Pack Manageer Demo 2")
    Label(window,text="Blue",bg="blue").pack(side=LEFT)
    ##side是控件定义停靠在父组件的哪一边上。
    Label(window,text="Red",bg='red').pack(side=LEFT,fill=BOTH,expand=1)
    ##fill参数使用BOTH、X、Y三个参数来说明在水平、垂直或两者上进行填充
    ##expand参数
    Label(window,text="Green",bg='green').pack(side=LEFT,fill=BOTH)
    window.mainloop()
PackManagerDemo()
