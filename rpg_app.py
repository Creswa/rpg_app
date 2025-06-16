import tkinter as tk
from tkinter import ttk
from frames import TopFrame, MidFrame, BottomFrame, NewSkill



class App(tk.Tk): #tento řádek a dva pod ním = window = tk.Tk()
    def __init__(self, title, size):

        #main setup
        super().__init__()
        self.title(title) # = window.title
        self.geometry(f"{size[0]}x{size[1]}")
        self.minsize(size[0], size[1])

        self.new_skill_name = tk.StringVar(value = "Enter new skill name")

        # widgets
        self.TopFrame = TopFrame(self)
        self.MidFrame = MidFrame(self)
        self.BottomFrame = BottomFrame(self)

        #run
        self.mainloop() # = window.mainloop()
        

# instance   
App("Class based app", (800,800)) #instance of the class App



