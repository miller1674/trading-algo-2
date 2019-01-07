from tkinter import *

class Application(Frame):
    def say_hi(self):
        print ("hi there, everyone!")

    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "left"})

        self._hi_there = Button(self)
        self._hi_there["text"] = "Hello",
        self._hi_there["command"] = self.say_hi
        self._hi_there.pack({"side": "left"})

        self._label= Label(self)
        self._label["text"] = "Algo Trading Stratety v1"
        self._label.pack()
        
        self._T = Text(root, height=2, width=30)
        self._T.pack()
        self._T.insert(END, "Just a text Widget\nin two lines\n")
        
        
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self._currentStock=[]
        self.createWidgets()
        

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()