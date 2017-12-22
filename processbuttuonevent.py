from Tkinter import *
class ProcessButtonEvent():
    def __init__(self):
        window=Tk()
        btok=Button(window,text='ok',fg='red',command=self.processOk)
        btcancel=Button(window,text='cancel',fg='blue',command=self.processCancel)
        btok.pack()
        btcancel.pack()
        window.mainloop()
    def processOk(self):
        print 'Ok button is clicked'
    def processCancel(self):
        print 'Cancel button is clicked'

ProcessButtonEvent()
