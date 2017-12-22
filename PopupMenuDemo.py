# -*- coding:utf-8 -*-
from Tkinter import *
class PopupMenuDemo():
    def __init__(self):
        window=Tk()
        window.title("Popup Menu Demo")
        self.menu=Menu(window,tearoff=0)
        self.menu.add_command(label="Draw a line",command=self.displayLine)
        self.menu.add_command(label="Draw a rectangle",command=self.displayRect)
        self.menu.add_command(label="Clear",command=self.clearCanvas)

        self.canvas=Canvas(window,width=200,height=100,bg="white")
        self.canvas.pack()
        self.canvas.bind("<Button-3>",self.popup)
        
        window.mainloop()

    def displayRect(self):
        pass

    def displayOval(self):
        pass

    def displayLine(self):
        pass

    def clearCanvas(self):
        pass

    def popup(self,event):
        self.menu.post(event.x_root,event.y_root)
     
        
        
PopupMenuDemo()
