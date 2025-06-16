import tkinter as tk
from tkinter import ttk
from frames import TopFrame, MidFrame, BottomFrame, NewSkill
import random


class App(tk.Tk):
    def __init__(self, title, size):
        super().__init__()

        # Main window setup
        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}")
        self.minsize(size[0], size[1])

        # Shared variables
        self.new_skill_name = tk.StringVar(value="Enter new skill name")
        self.experience = tk.IntVar(value = 0)
        self.level = tk.IntVar(value = 1)

        # Frames
        self.top_frame = TopFrame(self)
        self.mid_frame = MidFrame(self)
        self.bottom_frame = BottomFrame(self, self.new_skill_name, self.create_new_skill)
        
        self.mainloop()

    def create_new_skill(self):
        name = self.new_skill_name.get().strip()
        if name:
            if len(name) > 25:
                print("Max 25 characters")
            else:
                NewSkill(self.mid_frame.skills_frame, name, self.level, self.experience)





if __name__ == "__main__":
    App("Class based app", (800, 800))
