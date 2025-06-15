import tkinter as tk
from tkinter import ttk

class App(tk.Tk): #tento řádek a dva pod ním = window = tk.Tk()
    def __init__(self, title, size):

        #main setup
        super().__init__()
        self.title(title) # = window.title
        self.geometry(f"{size[0]}x{size[1]}")
        self.minsize(size[0], size[1])

        self.New_skill = New_skill(self)

        self.mainloop()
        
class New_skill(ttk.Frame):
        def __init__(self, parent):
             super().__init__(parent)
             self.create_new_skill()
             self.pack(expand = False, fill = "x")

        def create_new_skill(self):
            ## new skill
            new_skill_frame = ttk.Frame(self, height = 50, borderwidth = 5, relief="solid")
            new_skill_frame.pack_propagate(False)
            new_skill_frame.pack(side = "top", fill = "x", expand = False)

            # new skill frame grid
            new_skill_frame.columnconfigure((0,1), weight = 2)
            new_skill_frame.columnconfigure((2,3), weight = 1, uniform="a")
            new_skill_frame.rowconfigure((0,1), weight=1)

            #new_skill_name_input = new_skill_name.get()

            skill_name = ttk.Label(new_skill_frame, text = "Something", anchor="w", borderwidth=1, relief="solid")
            level = ttk.Label(new_skill_frame, text="Level", anchor="w", borderwidth=1, relief="solid")
            mninus_button = ttk.Button(new_skill_frame, text="+")
            plus_button = ttk.Button(new_skill_frame, text="-")
            level_bar = ttk.Label(new_skill_frame, text="Level progress", anchor="center", borderwidth=2, relief="solid")

            #placement to grid
            skill_name.grid(column = 0, sticky = "nsew")
            level.grid(row = 0, column = 1, sticky = "nsew")
            mninus_button.grid(row = 0, column = 2, sticky = "nsew")
            plus_button.grid(row = 0, column = 3, sticky = "nsew")
            level_bar.grid(row = 1, column = 0, columnspan = 4, sticky = "nsew")  

App("Class", (800,800))