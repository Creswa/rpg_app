import tkinter as tk
from tkinter import ttk


class App(tk.Tk): #tento řádek a dva pod ním = window = tk.Tk()
    def __init__(self, title, size):

        #main setup
        super().__init__()
        self.title(title) # = window.title
        self.geometry(f"{size[0]}x{size[1]}")
        self.minsize(size[0], size[1])

        global new_skill_name
        new_skill_name = tk.StringVar(value = "Enter new skill name")

        # widgets
        self.top_frame = top_frame(self)
        self.mid_frame = mid_frame(self)
        self.bottom_frame = bottom_frame(self)

        #run
        self.mainloop() # = window.mainloop()

class top_frame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_layout_and_widgets()
        self.pack(expand = False, fill = "x")

    def create_layout_and_widgets(self):
        # layout
        self.columnconfigure((0,1), weight = 1, uniform="a") #buď to i s placingem může být tady, nebo by se to dalo do jiné funkce a před všechno by se dalo self.name.grid(...)
        self.columnconfigure(2, weight = 2)

        # creating widgets
        name = tk.Label(self, text = 'Name:', background = 'red', anchor = "w")
        total_level = tk.Label(self, text = 'Level:', background = "purple", anchor = "w")

        # placing widgets
        name.grid(column = 0, sticky = "nsew")
        total_level.grid(row = 0, column = 1, sticky = "nsew")

class mid_frame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_layout_and_widgets()
        self.pack(expand = True, fill = "both")
    
    def create_layout_and_widgets(self):
        # layout
        global main_frame
        main_frame = tk.Frame(self)
        main_frame.pack(expand=True, fill="both")
        # create widgets

        # place widgets
        main_frame.pack(expand = True, fill = "both")

class bottom_frame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_layout_and_widgets()
        self.pack(expand = False, fill = "x")
            
    def create_layout_and_widgets(self):
        # layout
        self.columnconfigure(0, weight = 2)
        self.columnconfigure((1,2), weight = 1, uniform="a")

        # create widgets
        skill_name = ttk.Entry(self, textvariable = new_skill_name)
        add_skill_button = ttk.Button(self, text = 'Add skills', command = create_new_skill)
        delete_mode_button = ttk.Button(self, text = 'Delete mode')

        # place widgets 
        skill_name.grid(column = 0, sticky = "nsew")
        add_skill_button.grid(row = 0, column = 1, sticky = "nsew")
        delete_mode_button.grid(row = 0, column =2, sticky = "nsew")

class New_skill(ttk.Frame):
        def __init__(self, parent):
             super().__init__(parent)
             self.create()
             self.pack(expand = False, fill = "x")

        def create(self):
            ## new skill
            new_skill_frame = ttk.Frame(self, height = 50, borderwidth = 5, relief="solid")
            new_skill_frame.pack_propagate(False)
            new_skill_frame.pack(side = "top", fill = "x", expand = False)

            # new skill frame grid
            new_skill_frame.columnconfigure((0,1), weight = 2)
            new_skill_frame.columnconfigure((2,3), weight = 1, uniform="a")
            new_skill_frame.rowconfigure((0,1), weight=1)

            new_skill_name_input = new_skill_name.get()

            skill_name = ttk.Label(new_skill_frame, text = new_skill_name_input, anchor="w", borderwidth=1, relief="solid")
            level = ttk.Label(new_skill_frame, text="Level", anchor="w", borderwidth=1, relief="solid")
            mninus_button = ttk.Button(new_skill_frame, text="+")
            plus_button = ttk.Button(new_skill_frame, text="-")
            level_bar = tk.Label(new_skill_frame, text="Level progress", anchor="center", borderwidth=2, relief="solid", background = "red")

            #placement to grid
            skill_name.grid(column = 0, sticky = "nsew")
            level.grid(row = 0, column = 1, sticky = "nsew")
            mninus_button.grid(row = 0, column = 2, sticky = "nsew")
            plus_button.grid(row = 0, column = 3, sticky = "nsew")
            level_bar.grid(row = 1, column = 0, columnspan = 4, sticky = "nsew") 
        
 
def create_new_skill():
    if main_frame is not None:
       New_skill(main_frame)

# instance   
App("Class based app", (800,800)) #instance of the class App

#Poznámky
    #musím tvořit instance classy New_skill v okně main_frame, protože to je to okno, do kterého to chci dávat, ne třeba App.  App je sice parent, ale všech funkcí, přemýšlej, kam chceš tu danou věc umístit.


