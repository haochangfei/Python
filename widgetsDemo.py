# -*- coding:utf-8 -*-
from Tkinter import *

class WidgetDemo:
	def __init__(self):
		## create a window
		window=Tk()
		## set the title
		window.title("widgets Demo")
		## Add a checkbutton,radiobutton to a frame
		frame1=Frame(window)  ##Frame是一个框架控件，用于在屏幕上显示一个矩形区域，多用来作为容器
		frame1.pack()
		self.v1=IntVar()
		cbtBold=Checkbutton(frame1,text="Bold",variable=self.v1,command=self.processCheckbutton)
		## Checkbutton是多选框按钮
		self.v2=IntVar()
		rbRed=Radiobutton(frame1,text="Red",bg="Red",variable=self.v2,value=1,command=self.processRadiobutton)
		rbYellow=Radiobutton(frame1,text="Yellow",bg="Yellow",variable=self.v2,value=2,command=self.processRadiobutton)
		## Radiobutton是单选框按钮
		cbtBold.grid(row=1,column=1)
		rbRed.grid(row=1,column=2)
		rbYellow.grid(row=1,column=3)
		## grid是网格管理器，用于将控件放置在Frame1上
		
		frame2=Frame(window)
		frame2.pack()
		
		label=Label(frame2,text="Enter your name:")  ##Label是标签控件，用于显示文本或位图
		self.name=StringVar()
		entryName=Entry(frame2,textvariable=self.name)  ## Entry控件是输入控件，用于输入和显示文本
		btGetName=Button(frame2,text="Get Name",command=self.processButton)
		message=Message(frame2,text="It is a widgets demo")  ##Message是消息控件，用来显示多行文本，类似于Label
		label.grid(row=1,column=1)
		entryName.grid(row=1,column=2)
		btGetName.grid(row=1,column=3)
		message.grid(row=1,column=4)
		
		text=Text(window)  ##Text是文本控件，用于显示多行文本
		text.pack()
		text.insert(END,"Tip\nThe best way to learn Ikinter is to read")
		text.insert(END," these carefully designed example and use them")
		text.insert(END," to create your applications")
		
		window.mainloop()		
		
	def processCheckbutton(self):
		if self.v1.get()==1:
			print "check button is checked"
		else:
			print "check button is unchecked"
	def processRadiobutton(self):
		if self.v2.get()==1:
			print "Red is selected"
		else:
			print "Yellow is selected"
	def processButton(self):
		print "Your name is:"+self.name.get()
WidgetDemo()
