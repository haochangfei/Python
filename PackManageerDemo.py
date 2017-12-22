# -*- coding:utf-8 -*-
from Tkinter import *
class PackManagerDemo():
    def __init__(self):
        window=Tk()
        window.title("Pack Manageer Demo")
        Label(window,text="Blue",bg="blue").pack()
        Label(window,text="Red",bg='red').pack(fill=BOTH,expand=1)
        ##fill参数使用BOTH、X、Y三个参数来说明在水平、垂直或两者上进行填充
        ##expand参数
        Label(window,text="Green",bg='green').pack(fill=BOTH)
        window.mainloop()
PackManagerDemo()
