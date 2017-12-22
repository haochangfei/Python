# -*- coding:utf-8 -*-
from Tkinter import *
class MenuDemo():
    def __init__(self):
        window=Tk()
        window.title("Menu Demo")
        menubar=Menu(window)    ##创建一个菜单栏
        window.config(menu=menubar)     ##在窗口上显示菜单
        ##创建一个pull-down菜单，并添加到菜单栏
        operationMenu=Menu(menubar,tearoff=0)
        ##tearoff设置为0，说明不能被移出窗口
        menubar.add_cascade(label="operation",menu=operationMenu)
        operationMenu.add_command(label="Add",command=self.add)
        operationMenu.add_command(label="Subtract",command=self.subtract)
        operationMenu.add_separator()
        operationMenu.add_command(label="Multiply",command=self.multiply)
        operationMenu.add_command(label="Divide",command=self.divide)

        exitmenu=Menu(menubar,tearoff=0)
        menubar.add_cascade(label="Exit",menu=exitmenu)
        exitmenu.add_command(label="Quit",command=window.quit)

        frame0=Frame(window)
        frame0.grid(row=1,column=1,sticky=W)

        mainloop()

    def add(self):
        pass

    def subtract(self):
        pass

    def multiply(self):
        pass

    def divide(self):
        pass
        
        
        

MenuDemo()
