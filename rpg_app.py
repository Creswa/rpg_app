import tkinter as tk
from tkinter import ttk
from frames import TopFrame, MidFrame, BottomFrame, NewSkill


class App(tk.Tk):
    def __init__(self, title, size):
        super().__init__()

        # Main window setup
        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}")
        self.minsize(size[0], size[1])

        # Shared variables
        self.new_skill_name = tk.StringVar(value="Enter new skill name")
        self.experience = 0

        # Frames
        self.top_frame = TopFrame(self)
        self.mid_frame = MidFrame(self)
        self.bottom_frame = BottomFrame(self, self.new_skill_name, self.create_new_skill) 
        
        self.mainloop()

    def create_new_skill(self):
        name = self.new_skill_name.get().strip()
        if name:  # Don't create empty skills
            NewSkill(self.mid_frame.skills_frame, name, self.adding_exp, self.subtracting_exp)

    def adding_exp(self):
        self.experience += 1
        print(self.experience)
    
    def subtracting_exp(self):
        self.experience -= 1
        print(self.experience)
    
    def show_exp(self):
        print (self.experience)




if __name__ == "__main__":
    App("Class based app", (800, 800))
