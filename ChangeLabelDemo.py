##Import Ikinter
from Tkinter import *

class ChangeLabelDemo:
	def __init__(self):
		## create a window
		window=Tk()
		## set the title
		window.title("Change Label Demo")
		## Add a checkbutton,radiobutton to a frame
		frame1=Frame(window)
		frame1.pack()
		self.lb1=Label(frame1,text="Programming is fun")
		self.lb1.pack()
		
		frame2=Frame(window)
		frame2.pack()
		
		label=Label(frame2,text="Enter text:")
		self.msg=StringVar()
		entry=Entry(frame2,textvariable=self.msg)
		btchangeText=Button(frame2,text="Change Text",command=self.processButton)
		
		self.v1=StringVar()
		rbRed=Radiobutton(frame2,text="Red",bg="red",variable=self.v1,value="R",command=self.processRadiobutton)
		rbYellow=Radiobutton(frame2,text="Yellow",bg="yellow",variable=self.v1,value="Y",command=self.processRadiobutton)
		
		
		label.grid(row=1,column=1)
		entry.grid(row=1,column=2)
		btchangeText.grid(row=1,column=3)
		rbRed.grid(row=1,column=4)
		rbYellow.grid(row=1,column=5)		

		window.mainloop()		
		
	#def processCheckbutton(self):
		#if self.v1.get()==1:
			#print "check button is checked"
		#else:
			#print "check button is unchecked"
	def processRadiobutton(self):
		if self.v1.get()=="R":
			self.lb1["fg"]="red"
		elif self.v1.get()=="Y":
			self.lb1["fg"]="yellow"
	def processButton(self):
		self.lb1['text']=self.msg.get()
		
ChangeLabelDemo()
